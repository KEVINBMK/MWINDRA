# MWINDRA — Diagrammes avant développement (séquences, contexte, états)

Document de **référence** pour aligner l’équipe **électronique / embarqué** et **logiciel** avant le code.  
Complète [`SPEC_MVP_LOGICIEL_MWINDRA.md`](SPEC_MVP_LOGICIEL_MWINDRA.md).

**Où voir les diagrammes ?** Sur GitHub (rendu Mermaid) ou sur [mermaid.live](https://mermaid.live).

---

## 1) Synthèse des flux à implémenter

| # | Flux | Acteurs | Endpoint / action clé |
|---|------|---------|------------------------|
| F1 | Mesure radiation périodique | Bracelet → API | `POST /api/events` |
| F2 | Appui SOS | Bracelet → API | `POST /api/events` (`sos: true` ou `type: SOS`) |
| F3 | Affichage alertes live | Dashboard → API | `GET /api/alerts` |
| F4 | Détail d’un événement | Dashboard → API | `GET /api/events/{id}` |
| F5 | Confirmation / clôture | Superviseur → API | `PATCH /api/events/{id}` |
| F6 | Historique / export | Superviseur → API | `GET /api/events`, `GET .../export.csv` |
| F7 | (Option) File d’attente sans réseau | Bracelet (local) | Envoi différé `POST` |

---

## 2) Diagramme de contexte (système et acteurs)

```mermaid
flowchart LR
  subgraph Terrain["Terrain"]
    P[Porteur]
    B[Bracelet IoT]
  end
  subgraph SaaS["Plateforme MWINDRA"]
    API[API REST]
    DB[(Base de données)]
    UI[Dashboard web]
  end
  S[Superviseur / sécurité]

  P --> B
  B -->|"HTTPS JSON"| API
  API --> DB
  S --> UI
  UI -->|"HTTPS"| API
```

---

## 3) Diagramme de séquence — F1 : mesure radiation (envoi normal)

*Hypothèse : le bracelet a du réseau. Le serveur enregistre chaque mesure ; les alertes “liste rouge” peuvent être filtrées côté API.*

```mermaid
sequenceDiagram
  participant Porteur
  participant Bracelet as Bracelet ESP32
  participant Capteur as Capteur radiation
  participant API as API MWINDRA
  participant DB as Base SQLite

  Porteur->>Bracelet: Porte le dispositif
  Bracelet->>Capteur: Lire mesure
  Capteur-->>Bracelet: Valeur brute
  Note over Bracelet: Option A : niveau GREEN/YELLOW/RED sur le bracelet<br/>Option B : envoi valeur seule, niveau calculé serveur
  Bracelet->>API: POST /api/events (JSON + Bearer token)
  API->>API: Valider token + schéma
  API->>DB: INSERT event
  DB-->>API: OK
  API-->>Bracelet: 201 Created { id }
```

---

## 4) Diagramme de séquence — F2 : urgence SOS

```mermaid
sequenceDiagram
  participant Porteur
  participant Bracelet as Bracelet ESP32
  participant API as API MWINDRA
  participant DB as Base SQLite

  Porteur->>Bracelet: Appui bouton SOS
  Bracelet->>Bracelet: Bip / LED urgence (local)
  Bracelet->>API: POST /api/events (sos:true, type:SOS, lat,lng...)
  API->>DB: INSERT event (status SUSPECT)
  API-->>Bracelet: 201 Created
  Note over API,DB: L’alerte apparaît via GET /api/alerts
```

---

## 5) Diagramme de séquence — F3 : tableau de bord (rafraîchissement)

*MVP classique : polling toutes les 2–5 s. Le WebSocket peut être une V2.*

```mermaid
sequenceDiagram
  participant Sup as Superviseur
  participant Nav as Navigateur
  participant API as API MWINDRA
  participant DB as Base SQLite

  loop Toutes les 2 à 5 secondes
    Nav->>API: GET /api/alerts?limit=50
    API->>DB: SELECT (RED + SOS)
    DB-->>API: Lignes
    API-->>Nav: JSON liste alertes
    Nav-->>Sup: Affichage mis à jour
  end
```

---

## 6) Diagramme de séquence — F4 + F5 : ouvrir le détail puis confirmer

```mermaid
sequenceDiagram
  participant Sup as Superviseur
  participant Nav as Navigateur
  participant API as API MWINDRA
  participant DB as Base SQLite

  Sup->>Nav: Clic sur une alerte
  Nav->>API: GET /api/events/{id}
  API->>DB: SELECT par id
  DB-->>API: Event
  API-->>Nav: JSON détail
  Nav-->>Sup: Écran détail (carte / lat-lng)

  Sup->>Nav: Confirmer / résoudre + note
  Nav->>API: PATCH /api/events/{id} (status, note)
  API->>DB: UPDATE
  API-->>Nav: 200 OK
```

---

## 7) Diagramme de séquence — F6 : historique et export CSV

```mermaid
sequenceDiagram
  participant Sup as Superviseur
  participant Nav as Navigateur
  participant API as API MWINDRA
  participant DB as Base SQLite

  Sup->>Nav: Filtres date / bracelet
  Nav->>API: GET /api/events?from=&to=&braceletId=
  API->>DB: SELECT filtré
  DB-->>API: Résultats
  API-->>Nav: JSON

  Sup->>Nav: Export CSV
  Nav->>API: GET /api/events/export.csv?...
  API->>DB: SELECT
  API-->>Nav: Fichier CSV
```

---

## 8) Diagramme de séquence — F7 (option) : pas de réseau puis renvoi

*À n’implémenter que si vous le tranchez dans la spec ; sinon mentionner comme “phase 2” au jury.*

```mermaid
sequenceDiagram
  participant Bracelet as Bracelet ESP32
  participant Memo as Mémoire locale
  participant API as API MWINDRA

  Bracelet->>API: POST /api/events
  API-->>Bracelet: Erreur / timeout
  Bracelet->>Memo: Stocker événement (file)
  Note over Bracelet: Alerte locale LED/bip reste active si critique
  Bracelet->>API: Réseau revenu : rejouer POST
  API-->>Bracelet: 201 Created
  Bracelet->>Memo: Supprimer de la file
```

---

## 9) Machine à états — statut d’un événement d’alerte

```mermaid
stateDiagram-v2
  [*] --> SUSPECT: Création (RED ou SOS)
  SUSPECT --> CONFIRMED: Superviseur confirme
  SUSPECT --> RESOLVED: Clôture directe (option)
  CONFIRMED --> RESOLVED: Incident terminé
  RESOLVED --> [*]
```

*Les mesures GREEN/YELLOW peuvent rester sans cycle SUSPECT si vous ne les traitez pas comme “alertes” dans `GET /api/alerts`.*

---

## 10) Modèle de données simplifié (ER)

```mermaid
erDiagram
  BRACELET ||--o{ EVENT : envoie
  BRACELET {
    string braceletId PK
    string label
    datetime createdAt
  }
  EVENT {
    int id PK
    string braceletId FK
    string type
    float radiationValue
    string radiationUnit
    string level
    float lat
    float lng
    datetime timestamp
    string status
    string note
  }
```

---

## 11) Déploiement MVP (vue simple)

```mermaid
flowchart TB
  subgraph Hebergeur["Machine / cloud MVP"]
    API[API + DB SQLite]
    UI[Fichiers dashboard]
  end
  B[Bracelets] -->|Internet| API
  U[Navigateur superviseur] -->|HTTP| API
  U --> UI
```

*Si API et UI sont sur le même processus (ex. FastAPI sert le `dist/` du front), une seule URL suffit.*

---

## 12) Checklist “on peut coder” (validation équipe)

- [ ] **Qui calcule le niveau** (bracelet vs serveur) est tranché.
- [ ] **Format JSON** `POST /api/events` figé (champs obligatoires / optionnels).
- [ ] **Auth** : Bearer token partagé pour le bracelet (MVP).
- [ ] **Règle** : quand `GET /api/alerts` retourne une ligne (RED seulement ? RED+SOS ? jaune inclus ?).
- [ ] **Statuts** : `SUSPECT` → `CONFIRMED` / `RESOLVED` compris par tous.
- [ ] **Scénario démo** F1 + F2 + F5 répété sans erreur.

---

## 13) Légende des messages (exemple JSON minimal)

**Mesure radiation**

```json
{
  "braceletId": "BR-001",
  "timestamp": "2026-04-10T14:00:00Z",
  "type": "RADIATION",
  "radiationValue": 0.42,
  "radiationUnit": "uSv/h",
  "level": "YELLOW",
  "lat": -4.32,
  "lng": 15.31
}
```

**SOS**

```json
{
  "braceletId": "BR-001",
  "timestamp": "2026-04-10T14:02:00Z",
  "type": "SOS",
  "sos": true,
  "lat": -4.32,
  "lng": 15.31
}
```

---

*Fin du document — à versionner avec le reste du repo MWINDRA.*
