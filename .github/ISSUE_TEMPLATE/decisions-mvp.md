---
name: Décisions MVP
about: Alignement équipe — cocher les choix du MVP logiciel (cases interactives)
title: "Décisions MVP"
---

## Comment utiliser cette issue

1. Cliquez sur **Submit** pour créer l’issue (vous pouvez garder le titre **Décisions MVP**).
2. Cochez les cases directement dans la description : **GitHub enregistre les coches** sur cette issue.
3. Référence doc : [SPEC_MVP_LOGICIEL_MWINDRA.md](https://github.com/KEVINBMK/MWINDRA/blob/main/SPEC_MVP_LOGICIEL_MWINDRA.md)

---

### Utilisateur principal (choisir une seule option)

- [ ] Responsable sécurité
- [ ] Superviseur terrain
- [ ] Inspecteur
- [ ] Autre (préciser en commentaire)

### Internet pendant la démo (choisir une seule option)

- [ ] Oui, stable
- [ ] Non / instable

### Si internet instable — plan B (plusieurs choix possibles)

- [ ] Réseau local (PC + hotspot)
- [ ] Pas de carte, seulement lat/lng + zone
- [ ] Simulation des données (script local)

### GPS (choisir une seule option)

- [ ] Oui (coordonnées)
- [ ] Non (ou pas fiable)

### Affichage de la position (choisir une seule option)

- [ ] Carte (si internet disponible)
- [ ] Texte (lat/lng + zone)

### Alertes incluses dans le MVP (cocher ce qu’on fait vraiment)

- [ ] Radiation (jaune / rouge)
- [ ] SOS (bouton urgence)

### Le jaune est… (choisir une seule option)

- [ ] Un simple avertissement (pas une alerte “critique”)
- [ ] Une alerte comme les autres

### Backend (choisir une seule option)

- [ ] Python FastAPI
- [ ] Node.js Express
- [ ] Autre (préciser en commentaire)

### Base de données (choisir une seule option)

- [ ] SQLite (recommandé MVP)
- [ ] Postgres
- [ ] Autre (préciser en commentaire)

### Frontend dashboard (choisir une seule option)

- [ ] React + Vite
- [ ] HTML + Bootstrap (ultra simple)
- [ ] Autre (préciser en commentaire)

### Niveau GREEN / YELLOW / RED calculé par (choisir une seule option)

- [ ] Le bracelet
- [ ] Le serveur (recommandé pour centraliser les seuils)

### Hébergement du dashboard (choisir une seule option)

- [ ] Même serveur que l’API (recommandé MVP)
- [ ] Serveur / déploiement séparé

### Notifications externes (email, Telegram, etc.) (choisir une seule option)

- [ ] Oui
- [ ] Non (dashboard uniquement pour le MVP)

### Preuve d’intégrité — chaîne de hash sur les événements (choisir une seule option)

- [ ] Oui
- [ ] Non

### Afficher le nom du mineur sur le dashboard (choisir une seule option)

- [ ] Oui
- [ ] Non (recommandé : afficher seulement l’ID bracelet, ex. BR-001)

---

## À compléter en commentaire (ou éditer la description)

- **Objectif en 2 minutes (1 phrase)** :
- **Seuils radiation (provisoires)** — unité : … / vert (inférieur à …) / jaune (à partir de …) / rouge (à partir de …)
- **Format ID bracelet** (ex. BR-001) :
- **Fréquence d’envoi des données** (ex. toutes les 10–30 s, ou seulement sur alerte) :

---

### Suivi rapide (optionnel)

- [ ] Scénario démo A (radiation rouge) testé
- [ ] Scénario démo B (SOS) testé
- [ ] Export CSV / historique validé pour le jury
