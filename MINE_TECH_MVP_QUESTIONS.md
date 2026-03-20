## Mine Tech - Questions pour cadrer le MVP (4-5 jours)

Objectif: transformer l'idee "collier IoT (alerte terrain) + logiciel de detection/traçabilite de fraude minerale" en un MVP presentable au concours.

---

### 1) Problème exact et priorite
1. Pour qui on construit en priorite: mineurs, superviseurs, inspecteurs, acheteurs/exportateurs, ou autorites?
2. Qu'est-ce que la "fraude minerale" signifie dans votre MVP (definir en 1 phrase): ex. presence en zone interdite, exploitation non autorisee, mineurs non enregistres, export sans traçabilite, etc.
3. Quel evenement declenche une alerte (1 exemple concret): ex. entree en zone interdite, air dangereux, choc/instabilite probable, non-respect horaire, etc.
4. Qui recoit l'alerte et que fait-il apres (decision/validation/controle)?

---

### 2) MVP: limites concretes (pour tenir en 4-5 jours)
5. MVP = demo preuve de concept (limitee) ou produit robuste (qualite elevee)?
6. Vos 3 "must-have" (max): 
   - capteurs/mesures
   - alerte temps reel (ou quasi temps reel)
   - tableau de bord / rapport
7. Qu'est-ce que vous excluez volontairement du MVP (blocker volontairement): ex. blockchain reelle publique, drones, IA complexe, cartographie complete, etc.

---

### 3) Donnees terrain: quoi mesurer vraiment
8. Quels capteurs vous pouvez avoir rapidement et realistement?
   - GPS (oui/non)
   - temperature + humidite (oui/non)
   - qualite de l'air (lequel: CO, H2S, particules, etc.)
   - chocs/eboulement (accelerometre / IMU)
   - bouton SOS (oui/non)
9. Si vous n'avez pas tous les capteurs, quel "signal proxy" vous utilisez pour l'alerte de fraude/risque? (ex: accelerations anormales + geofencing)
10. Frequence d'envoi: toutes les X secondes/minutes, ou uniquement en cas d'alerte?
11. Fonctionnement reseau: offline (stockage local) accepte, ou reseau continu obligatoire?

---

### 4) Detection: regles simples d'abord (recommandation MVP)
12. Quelle regle simple de detection vous implementez en premier?
   - Geofencing: presence dans zone interdite
   - Identite: badge/ID non enregistres
   - Conformite: hors horaires du permis
   - Comportement anormal: mouvement/choc incoherent
13. Comment definissez-vous les zones interdites dans le MVP: points GPS, polygones, rayons?
14. Alarme "suspect" vs "confirmee": que choisissez-vous pour le jury?
15. Anti-faux positifs minimal: seuil, duree minimale, moyenne/filtre (comment?)

---

### 5) Traçabilite: faut-il une blockchain pour le concours?
16. Le concours exige-t-il une blockchain reelle, ou une preuve de trace (journal immuable/audit log) suffit?
17. En MVP, acceptez-vous une alternative plus rapide:
   - journal append-only signe (hash chain) cote serveur
   - ou event store avec empreintes (hash) et horodatage
18. Quel lien concret entre "collier" et "evenement" et "lot/minerai" en MVP?
   - Exemple: scan QR a des points fixes -> creation d'un event signed

---

### 6) Identites & securite (indispensable meme en demo)
19. Comment identifiez-vous un mineur dans votre MVP: ID unique, QR du collier, ou badge?
20. Comment reduisez-vous l'usurpation:
   - authentification au scan + secret/cle
   - validation sur serveur avec cle publique
21. Donnees sensibles: quelles donnees vous devez anonymiser dans le dashboard?
22. Droits d'acces: admin, inspecteur, superviseur (qui voit quoi?)

---

### 7) La demo pour le jury (scenario de 3 minutes)
23. Scenario de demo en etapes (ex: 1 minute acquisition, 2 minutes detection/trace, 30 secondes preuve).
24. Quelles preuves visuelles presenterez-vous:
   - chronologie des evenements
   - carte/geofencing simplifie
   - details de l'alerte (capteur, temps, localisation)
   - export CSV/PDF (si possible)
25. "Definition of done": quelles caracteristiques valident que le MVP est pret?

---

### 8) Pile technique (choix rapides pour eviter de se perdre)
26. Hardware cible (meme si c'est une maquette):
   - ESP32 (oui/non)
   - autre (lequel?)
27. Backend: Node/Express, Python/FastAPI, autre?
28. Frontend: dashboard web simple? appli mobile?
29. Donnees: format (JSON), stockage (SQLite), API (REST)?
30. Deploiement: local seulement ou accessible en reseau?

---

## Les 6 questions a repondre tout de suite (priorite absolue)
1. Votre definition MVP de la "fraude" = quoi exactement (1 phrase)?
2. Capteur(s) obligatoire(s) pour declencher l'alerte (GPS est-il obligatoire)?
3. Reseau sur site: disponible (WiFi/4G) ou non?
4. Alerte instantanee ou par lots (toutes les X minutes)?
5. Traçabilite: acceptez-vous un journal immuable sans blockchain publique?
6. Equipe: quelle pile technique vous maitrisez le plus (ESP32 + Node/React, etc.)?

---

## Case a remplir (suivi equipe)
- Cible prioritaire:
- Definition fraude (1 phrase):
- Evenement declencheur (1 exemple):
- Regle de detection MVP:
- Zones interdites (comment definies):
- Capteurs retenus:
- Frequence d'envoi:
- Type de traçabilite en MVP:
- Scenario de demo (3 minutes):

