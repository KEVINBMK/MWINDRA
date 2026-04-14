# Simulation MWINDRA (100 % fictive)

Deux pages web + une petite API **sans bracelet** : pour répéter la démo devant le jury (2 téléphones + 1 PC).

## Prérequis

- Python **3.10+** recommandé  
- PC et téléphones sur le **même réseau Wi‑Fi** (ou partage de connexion depuis le PC)

## Installation

```bash
cd simulation
python -m pip install -r requirements.txt
```

## Lancer le serveur

```bash
cd simulation
python server.py
```

Le serveur écoute sur **`http://0.0.0.0:8000`** (toutes les interfaces).

## Adresses sur les téléphones

1. Sur le PC, notez l’adresse IPv4 du Wi‑Fi (ex. `192.168.1.20`).  
2. **Téléphone A (bracelet)** : `http://192.168.1.20:8000/bracelet`  
3. **Téléphone B (superviseur)** : `http://192.168.1.20:8000/superviseur`  
4. Page d’accueil : `http://192.168.1.20:8000/`

Sous Windows, autoriser **Python** dans le pare-feu pour le port **8000** (privé) si les téléphones ne chargent pas la page.

## Token démo (Bearer)

Valeur par défaut : **`demo-mwindra-2026`**

Pour changer : variable d’environnement `MWINDRA_DEMO_TOKEN` avant de lancer `server.py`.

## Seuils affichés (démo uniquement)

Voir `static/seuils-demo.txt` et `GET /api/config/seuils`.

## Scénario rapide

1. **Téléphone A** : glisser le curseur vers le **rouge** → **Envoyer la mesure**, ou utiliser **Niveau aléatoire** / **Pic aléatoire** / **Envoyer mesure aléatoire** pour la démo.  
2. **Téléphone B** : l’alerte apparaît dans **Alertes** (rafraîchissement ~2 s).  
3. **Téléphone A** : appuyer sur **SOS**.  
4. **Téléphone B** : cliquer sur une ligne → **Confirmer** / **Résolu**.

Les données sont stockées **en mémoire** : elles disparaissent si vous arrêtez le serveur.
