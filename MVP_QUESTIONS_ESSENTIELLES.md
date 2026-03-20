## MVP - Questions essentielles (a completer pour la demo)

Objectif: en 4-5 jours, repondre a ces questions pour que le projet soit presentable, coherent et testable.

---

## 1) Demarche du MVP (1 parcours utilisateur)
1. Quel est le seul utilisateur du MVP pour la demo (inspecteur, responsable, superviseur, mineur, etc.)?
2. Decrire le parcours complet en 5 etapes max (ex: scan ID -> collecte capteur -> detection -> alerte -> preuve/rapport).
3. Quel est l'element qui prouve que “ca marche” au jury (carte geofence, timeline, compteur alertes, export, etc.)?

---

## 2) Fraude et risque: definition non ambigu"
4. Definition exacte du mot “fraude” dans votre MVP (1 phrase).
5. Liste des types d'evenements que vous allez gerer (max 2 pour le MVP).
6. Pour chaque evenement: quelle regle declenche (regle simple) + quel seuil (valeur) + quelle duree minimale (minutes/secondes)?
7. Qu'est-ce qui marque un evenement comme “suspect” vs “confirmee” (meme si la confirmation est manuelle en demo)?

---

## 3) Geofencing (si vous utilisez le GPS)
8. Les zones interdites sont definies comment (liste de points, cercle rayon, ou polygone)?
9. Quelle est la methode de test pour la demo (ex: faire entrer/sortir le collier depuis 2 points GPS predefinis)?
10. Quelle marge GPS acceptez-vous pour eviter les faux positifs (ex: 20-50m selon le materiel)?
11. Combien de temps une personne doit rester dans la zone pour declencher une alerte (ex: 10s, 30s, 2min)?

---

## 4) Capteurs: minimum viable
12. Capteurs retenus (liste courte) et pourquoi (lien direct avec vos 2 evenements maximum).
13. Quelles mesures sont en entree ML (si ML) et lesquelles sont “regles”?
14. Comment vous allez simuler les donnees pour la demo (fichier CSV, script, ou dataset artificiel)?
15. Frequence d'envoi des donnees (toutes les X secondes/minutes) et taille des messages (pour eviter saturation).

---

## 5) ML (si vous voulez vraiment en montrer)
16. Quel modele ML voulez-vous montrer (anomalie, classification, detection de choc, prediction simple)?
17. Taille cible du modele: (option) modele tres petit / inference rapide sur Raspberry Pi.
18. Les donnees ML viennent d'ou (capteurs reels, simulation, dataset public, ou enregistrement sur site)?
19. Comment vous evaluerez rapidement le modele en demo (precision/recall simplifie, ou “taux de detection” sur 10 essais)?
20. Decrivez le pipeline ML en 3 lignes (input -> inference -> score -> seuil -> evenement).

---

## 6) Tra"cabilite / preuve d'integrite (sans bloquer sur la blockchain)
21. Qu'est-ce que vous stockez exactement pour chaque evenement (champ de base minimum)?
22. Quel mecanisme d'immutabilite utilisez-vous pour le MVP (hash chain / signature / log append-only)?
23. Qui peut acceder au journal (admin/inspecteur) et comment l'export se fait (CSV/PDF)?
24. Comment prouver au jury que l'historique n'a pas ete modifie (afficher prev_hash + hash actuel + horodatage)?

---

## 7) Securite & anti-usurpation (minimum raisonnable)
25. Comment identifiez-vous le mineur (ID unique, QR collier, badge)?
26. Comment eviter qu'on “copie” un ID (secret/cle cote serveur, challenge simple, etc.)?
27. Comment vous gerez le cas “pas de reseau” (cache local + envoi plus tard, ou alerte locale)?
28. Quelle donnee doit rester privee (ecraser/masquer lors du dashboard)?

---

## 8) Dashboard et reporting pour le jury
29. Quelles 4 vues allez-vous montrer (ex: liste evenements, details alerte, carte geofence simplifiee, export)?
30. Quels indicateurs de succes affichez-vous (nb alertes, delai detection, faux positifs estimés)?
31. Quels sont les messages d'alerte clairs (ex: “Zone interdite detectee - suspect” + timestamp + device ID)?

---

## 9) Validation terrain (meme si c'est une simulation au debut)
32. Combien d'essais de demo vous faites avant le jour du concours (ex: 10 scenarios)?
33. Pour chaque scenario: resultat attendu vs resultat observe.
34. Quelles erreurs frequentes voulez-vous prevenir (GPS instable, manque reseau, capteur bruit, delai upload)?

---

## 10) Plan 4-5 jours (check rapide)
35. Jour 1: hardware/test capteur + message JSON format + endpoint serveur.
36. Jour 2: regles detection + geofencing + creation evenement + hash chain.
37. Jour 3: dashboard + vue chronologie + export.
38. Jour 4: integrer simulation ML (optionnel) ou ameliorer seuil/anti-faux positif + securite ID.
39. Jour 5: polissage demo + video/test final + documentation simple.

---

## A completer (zone de saisie equipe)
- Evenement 1:
- Evenement 2:
- Regle even. 1 (seuil + duree):
- Regle even. 2 (seuil + duree):
- Zone interdite (definition + parametres):
- Capteurs retenus:
- Traçabilite (hash chain/signe):
- ML (oui/non + modele + seuil):
- Scenario demo final (5 etapes):

