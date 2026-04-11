## MWINDRA - SPEC MVP (COTE LOGICIEL)

Ce document sert a nous mettre d'accord, vite, avant de coder. Il contient des questions simples, des choix proposes, et une architecture MVP realiste en 4-5 jours.

Objectif demo: montrer qu'un bracelet envoie des donnees (radiation + SOS + position) et que la plateforme:

- recoit les donnees
- declenche/affiche des alertes claires
- localise rapidement le travailleur
- garde un historique exploitable (preuve / rapport)

### Comment utiliser ce document (equipe)

1. **Lire les sections 0 et 1** pour fixer le perimetre : utilisateur demo, internet, GPS, alertes, seuils, confidentialite.
2. **Trancher les choix** : cocher dans l’[issue « Decisions MVP »](https://github.com/KEVINBMK/MWINDRA/issues/new?template=decisions-mvp.md) (cases interactives), ou reporter les coches a la main dans ce fichier puis commit.
3. **Sections 2 a 7** : scenario de demo, architecture, donnees JSON, API, ecrans — servent de **cahier des charges** pour coder backend + dashboard.
4. **Sections 8 a 13** : options (notifications, hash-chain), planning 4–5 jours, tests, definition of done — a suivre pour livrer a temps.
5. **Avant de coder** : parcourir [`DIAGRAMMES_MVP_PRE_DEV.md`](DIAGRAMMES_MVP_PRE_DEV.md) (sequences, contexte, etats, checklist).

---

## 0) Regles du MVP (pour ne pas se perdre)

- MVP = 1 scenario demo + 3 fonctionnalites max.
- On prefere "simple et fiable" a "complexe et fragile".
- On annonce les features "future" (IA, capteurs gaz, etc.) dans la partie perspectives, pas dans le MVP.
- Tout ce qui n'aide pas la demo, on repousse apres.

---

## 1) Questions d'accord (a remplir ensemble)

### 1.1 Qui utilise le logiciel pendant la demo?

- **Choix unique (cocher 1) - Utilisateur principal**
  - [ ] Responsable securite
  - [ ] Superviseur terrain
  - [ ] Inspecteur
  - [ ] Autre: ______________________
- **Objectif en 2 minutes (remplir 1 phrase)**
  - Je veux pouvoir: _______________________________________________________
- **Parcours demo (5 etapes max)**
  - Etape 1: ____________________
  - Etape 2: ____________________
  - Etape 3: ____________________
  - Etape 4: ____________________
  - Etape 5: ____________________

### 1.2 Quels sont les 2 types d'alertes MVP?

Choix recommande:

- [ ] Radiation (jaune/rouge)
- [ ] SOS (bouton urgence)

Questions:

- Est-ce qu'on gere d'autres alertes au MVP? (NON recommande)
- Est-ce que "jaune" est une alerte ou juste un avertissement?

### 1.3 Internet pendant la demo?

- **Choix unique (cocher 1) - Internet**
  - [ ] Oui, internet stable
  - [ ] Non, internet instable / pas garanti
- **Si internet instable (choix multiples) - Plan B**
  - [ ] Reseau local (PC + hotspot)
  - [ ] Pas de carte, juste lat/lng + zone
  - [ ] Simulation donnees depuis un script local
  - [ ] Autre: ______________________

### 1.4 Localisation: GPS ou approximation?

- **Choix unique (cocher 1) - GPS**
  - [ ] Oui, GPS disponible (coordonnees)
  - [ ] Non, pas de GPS (ou pas fiable)
- **Choix unique (cocher 1) - Affichage position**
  - [ ] Carte (si internet)
  - [ ] Texte (lat/lng + zone)

### 1.5 Seuils radiation (meme provisoires)

On doit choisir des seuils pour la demo, meme si ce sont des valeurs "de presentation".

- Unite (ex: uSv/h): ____________________
- Vert: < ______
- Jaune: >= ______
- Rouge: >= ______

Important:

- Si on n'a pas le capteur reel au debut, on simule les valeurs et on garde les memes seuils.

### 1.6 Identifiants et privacy

- Format ID bracelet (ex: BR-001): ________
- **Choix unique (cocher 1) - Afficher le nom du mineur?**
  - [ ] Oui (nom visible dans le dashboard)
  - [ ] Non (recommande: on affiche seulement BR-001)
- Donnees sensibles a cacher: ______________________

---

## 2) Scenario de demo (script)

Remplir ce petit scenario. Il doit etre repetable.

### Scenario A - Radiation rouge

1. Le bracelet envoie une mesure normale (vert).
2. La radiation monte (jaune) -> affichage.
3. La radiation passe rouge -> alerte rouge.
4. Le responsable clique l'alerte -> voit details + position.
5. Le responsable confirme -> statut "CONFIRMED".
6. On montre l'historique + export CSV.

### Scenario B - SOS

1. Le mineur appuie sur SOS -> alerte immediatement visible.
2. On clique -> details + position + note.
3. On marque "RESOLVED".

Temps cible:

- Alerte visible au dashboard en < 5 secondes (ideal).

---

## 3) Architecture logicielle MVP (simple)

### 3.1 Blocs

- Bracelet (ESP32): lit capteur(s) -> envoie JSON
- Backend (API): recoit, valide, stocke, expose endpoints
- Dashboard web: affiche alertes + details + historique + export

### 3.2 Choix techno recommandes (rapide)

Option A (recommandee pour MVP):

- Backend: Python FastAPI
- DB: SQLite (fichier .db)
- Front: React + Vite (ou HTML/Bootstrap si on veut encore plus simple)

Option B (si equipe plus a l'aise):

- Backend: Node.js + Express
- DB: SQLite ou Postgres
- Front: React

Decision equipe:

- **Choix unique (cocher 1) - Backend**
  - [ ] Python FastAPI
  - [ ] Node.js + Express
  - [ ] Autre: ______________________
- **Choix unique (cocher 1) - Base de donnees**
  - [ ] SQLite (recommande MVP)
  - [ ] Postgres
  - [ ] Autre: ______________________
- **Choix unique (cocher 1) - Frontend**
  - [ ] React + Vite
  - [ ] HTML + Bootstrap (ultra simple)
  - [ ] Autre: ______________________

---

## 4) Donnees (contrat JSON) - ce que le bracelet envoie

On fixe un format stable. Meme si on simule, on respecte ce format.

### 4.1 Exemple de message (event)

- braceletId: "BR-001"
- timestamp: "2026-03-20T12:00:00Z" (ou heure locale ISO)
- type: "RADIATION" ou "SOS"
- radiationValue: nombre (si type=RADIATION)
- radiationUnit: "uSv/h"
- level: "GREEN" | "YELLOW" | "RED"
- lat: nombre (optionnel)
- lng: nombre (optionnel)
- battery: pourcentage (optionnel)
- sos: true/false (optionnel si type=SOS)

Questions:

- Le niveau (GREEN/YELLOW/RED) est calcule par le bracelet ou par le serveur?
  - Bracelet
  - Serveur (recommande si on veut centraliser les seuils)

---

## 5) Base de donnees (minimum)

### 5.1 Table bracelets (minimum)

- braceletId (unique)
- label (optionnel)
- createdAt

### 5.2 Table events (minimum)

- id (unique)
- braceletId
- type (RADIATION/SOS)
- radiationValue (nullable)
- radiationUnit
- level (GREEN/YELLOW/RED)
- lat/lng (nullable)
- timestamp (date/heure event)
- status (SUSPECT/CONFIRMED/RESOLVED)
- note (optionnel)

Regles:

- Un event rouge ou SOS = status "SUSPECT" au debut.
- Un responsable peut confirmer ou resoudre.

---

## 6) API (endpoints MVP)

On garde peu d'endpoints pour livrer vite.

### 6.1 Auth simple (MVP)

Choix MVP:

- une cle API statique (Bearer token) pour accepter les donnees bracelet.

### 6.2 Endpoints

- POST /api/events
  - recoit un event
  - cree un event en DB
  - retourne OK
- GET /api/alerts?limit=50
  - retourne seulement les events importants (RED + SOS)
- GET /api/events?braceletId=&from=&to=&limit=
  - historique
- GET /api/events/{id}
  - details
- PATCH /api/events/{id}
  - modifier status (CONFIRMED/RESOLVED) + note
- GET /api/events/export.csv?from=&to=&braceletId=
  - export (bonus utile)

Question:

- **Choix unique (cocher 1) - Hebergement dashboard**
  - [ ] Dashboard sur le meme serveur que l'API (recommande MVP)
  - [ ] Dashboard separe

---

## 7) Dashboard (3 pages MVP)

### Page 1 - Alertes

- liste des alertes recentes (RED + SOS en haut)
- couleur niveau
- bouton "Details"
- bouton "Confirmer"

### Page 2 - Detail

- braceletId
- type (RADIATION/SOS)
- valeur + unite + niveau
- date/heure
- position (carte ou texte)
- statut + note + bouton "RESOLVED"

### Page 3 - Historique

- filtre date + bracelet
- tableau evenements
- export CSV

UX simple:

- Un message doit etre lisible pour non-technique: "Danger radiation - Rouge" / "SOS - Urgence".

---

## 8) Notification (optionnel)

Si on a le temps:

- une notification email/telegram.
Sinon:
- l'alerte sur le dashboard suffit pour le MVP.

Decision:

- **Choix unique (cocher 1) - Notifications externes**
  - [ ] Oui (email/telegram)
  - [ ] Non (dashboard seulement, MVP)

---

## 9) Integrite / preuve (option forte pour le jury)

Sans "blockchain" lourde, on peut faire une chaine de hash:

- prevHash + hash pour chaque event
- hash = SHA-256(prevHash + donnees + timestamp)

Avantage:

- on explique au jury: "si quelqu'un change l'historique, la chaine casse"

Decision:

- **Choix unique (cocher 1) - Hash-chain (preuve)**
  - [ ] Oui
  - [ ] Non

---

## 10) Plan de travail 4-5 jours (logiciel)

### Jour 1 - Flux de bout en bout

- creer backend + DB
- POST /api/events (ingestion)
- page Alertes (liste simple)
- simulateur d'envoi (script) si bracelet pas pret

### Jour 2 - Details + statuts

- page Detail
- PATCH status (CONFIRMED/RESOLVED)
- filtres basiques

### Jour 3 - Historique + export

- page Historique
- export CSV
- design propre

### Jour 4 - Integration + solidite demo

- integration bracelet ou simulation stable
- fixer seuils radiation
- tests scenario A/B

### Jour 5 - Presentation

- repeter la demo 10 fois
- capture ecran/video
- slide 1 page: probleme -> solution -> demo -> impact

---

## 11) Tests (a preparer)

On doit tester avant le concours.

Scenarios minimum:

1. RADIATION vert -> jaune (pas de panique)
2. jaune -> rouge (alerte rouge visible)
3. SOS (alerte immediate)
4. perte internet (si possible)
5. retour internet + envoi differe (si on le supporte)

Pour chaque scenario:

- Donnees envoyees:
- Resultat attendu:
- Resultat observe:

---

## 12) Repartition equipe (proposee)

- Backend (API + DB + export): ________
- Frontend (dashboard 3 pages): ________
- Integration (bracelet/simulateur + format JSON): ________
- Tests demo + slides: ________

---

## 13) Check final (Definition of Done)

Le MVP est "pret" si:

- on peut generer une alerte rouge et la voir au dashboard
- on peut generer un SOS et la voir au dashboard
- on peut ouvrir le detail et voir la position (au moins lat/lng)
- on peut confirmer/resoudre une alerte
- on peut voir l'historique et exporter CSV
- la demo est repetable (10 fois sans bug)

