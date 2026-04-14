"""
Simulation MWINDRA — API + stockage en mémoire (aucun capteur réel).
Seuils µSv/h : purement démonstratifs (voir static/seuils-demo.txt).
"""
from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any, Optional

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

# --- Seuils DÉMO (µSv/h) — ne pas utiliser pour décision réelle ---
SEUIL_VERT_MAX = 0.5
SEUIL_JAUNE_MAX = 2.0

API_TOKEN = os.environ.get("MWINDRA_DEMO_TOKEN", "demo-mwindra-2026")

app = FastAPI(title="MWINDRA Simulation API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_events: list[dict[str, Any]] = []
_next_id = 1


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def niveau_depuis_valeur(u_sv_per_h: float) -> str:
    if u_sv_per_h < SEUIL_VERT_MAX:
        return "GREEN"
    if u_sv_per_h < SEUIL_JAUNE_MAX:
        return "YELLOW"
    return "RED"


def _auth(authorization: str | None) -> None:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Authorization Bearer requis")
    token = authorization.split(" ", 1)[1].strip()
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token invalide")


class EventIn(BaseModel):
    braceletId: str = Field(..., min_length=1, max_length=64)
    timestamp: Optional[str] = None
    type: str = Field(..., pattern="^(RADIATION|SOS)$")
    radiationValue: Optional[float] = None
    radiationUnit: str = "uSv/h"
    level: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    battery: Optional[int] = Field(None, ge=0, le=100)
    sos: Optional[bool] = None


class PatchEvent(BaseModel):
    status: Optional[str] = None
    note: Optional[str] = Field(None, max_length=2000)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "simulation"}


@app.post("/api/events")
def post_event(
    body: EventIn,
    authorization: str | None = Header(None),
) -> dict[str, Any]:
    _auth(authorization)
    global _next_id

    if body.level is not None and body.level not in ("GREEN", "YELLOW", "RED"):
        raise HTTPException(400, "level doit etre GREEN, YELLOW ou RED")

    ts = body.timestamp or _utc_now_iso()
    level = body.level
    radiation_value = body.radiationValue

    if body.type == "SOS":
        level = "RED"
        radiation_value = radiation_value if radiation_value is not None else None
    else:
        if radiation_value is None:
            raise HTTPException(400, "radiationValue requis pour type RADIATION")
        level = level or niveau_depuis_valeur(radiation_value)

    is_alert = body.type == "SOS" or level == "RED"
    status = "SUSPECT" if is_alert else "INFO"

    row = {
        "id": _next_id,
        "braceletId": body.braceletId,
        "type": body.type,
        "radiationValue": radiation_value,
        "radiationUnit": body.radiationUnit,
        "level": level,
        "lat": body.lat,
        "lng": body.lng,
        "battery": body.battery,
        "sos": bool(body.sos) if body.sos is not None else (body.type == "SOS"),
        "timestamp": ts,
        "status": status,
        "note": None,
    }
    _events.insert(0, row)
    _next_id += 1
    return {"ok": True, "id": row["id"]}


@app.get("/api/alerts")
def get_alerts(limit: int = 50) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for e in _events:
        if e["type"] == "SOS" or e["level"] == "RED":
            out.append(e)
        if len(out) >= limit:
            break
    return out


@app.get("/api/events")
def list_events(
    braceletId: str | None = None,
    limit: int = 100,
) -> list[dict[str, Any]]:
    rows = _events
    if braceletId:
        rows = [e for e in rows if e["braceletId"] == braceletId]
    return rows[:limit]


@app.get("/api/events/{event_id}")
def get_event(event_id: int) -> dict[str, Any]:
    for e in _events:
        if e["id"] == event_id:
            return e
    raise HTTPException(404, "Event introuvable")


@app.patch("/api/events/{event_id}")
def patch_event(
    event_id: int,
    body: PatchEvent,
    authorization: str | None = Header(None),
) -> dict[str, Any]:
    _auth(authorization)
    if body.status is not None and body.status not in ("SUSPECT", "CONFIRMED", "RESOLVED"):
        raise HTTPException(400, "status invalide")
    for e in _events:
        if e["id"] == event_id:
            if body.status is not None:
                e["status"] = body.status
            if body.note is not None:
                e["note"] = body.note
            return e
    raise HTTPException(404, "Event introuvable")


@app.get("/api/config/seuils")
def get_seuils() -> dict[str, Any]:
    return {
        "unite": "uSv/h",
        "vert_max_exclusif": SEUIL_VERT_MAX,
        "jaune_max_exclusif": SEUIL_JAUNE_MAX,
        "rouge": ">= jaune_max",
        "avertissement": "Valeurs uniquement pour demonstration / simulation.",
    }


static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(os.path.join(static_dir, "index.html"))


@app.get("/bracelet")
def page_bracelet() -> FileResponse:
    return FileResponse(os.path.join(static_dir, "bracelet.html"))


@app.get("/superviseur")
def page_superviseur() -> FileResponse:
    return FileResponse(os.path.join(static_dir, "superviseur.html"))


@app.get("/simulation3d")
def page_simulation_3d() -> FileResponse:
    return FileResponse(os.path.join(static_dir, "simulation3d.html"))


@app.get("/presentation-jury")
def page_presentation_jury() -> FileResponse:
    return FileResponse(os.path.join(static_dir, "presentation-jury.html"))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8000")),
        reload=False,
    )
