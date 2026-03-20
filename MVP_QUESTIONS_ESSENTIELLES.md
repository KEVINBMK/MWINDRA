## MVP - Questions simples (pour la demo)

Objectif : en 4-5 jours, répondre à ces questions pour que le projet soit clair, testable et facile à montrer au jury.

---

## 1) Le parcours du MVP (1 utilisateur)
1. Qui utilise le système pendant la démo ? (inspecteur, responsable, superviseur, etc.)
2. Décrivez le chemin complet en 5 étapes max (ex : scanner l'ID -> capteurs -> détection -> alerte -> preuve/rapport).
3. Qu'est-ce qui prouve que “ça marche” ? (ex : liste des alertes, chronologie, export, carte simple)

---

## 2) Fraude / risque : définition facile
4. Dans votre projet, c'est quoi “fraude” ? (une phrase)
5. Quels événements vous allez gérer ? (max 2 événements pour le MVP)
6. Pour chaque événement, donnez la règle simple :
   - quoi on regarde (capteur/zone)
   - quelle valeur déclenche (ex : “> X”, “dans la zone depuis Y secondes”)
   - combien de temps avant d'alerter
7. Un événement peut être “suspect” puis “confirmé” : comment vous passez de l’un à l’autre ?

---

## 3) Zone interdite (si vous utilisez le GPS)
8. Comment vous définissez la zone interdite ? (point/cercle/rayon ou coordonnées GPS)
9. Comment vous testez pendant la démo ? (ex : faire entrer/sortir à partir de 2 endroits GPS)
10. Si le GPS se trompe un peu, vous acceptez quelle “marge” ? (ex : 20-50m selon votre matériel)
11. Combien de temps la personne doit rester dans la zone pour déclencher une alerte ? (ex : 10s / 30s / 2min)

---

## 4) Capteurs : le minimum
12. Quels capteurs vous gardez ? (liste courte) Et pourquoi ? (liens directs avec vos 2 événements)
13. Quelles données servent pour la détection “automatique” (règles) ?
14. Comment vous allez simuler des données si vous n'avez pas de capteurs au début ? (fichier, script, valeurs test)
15. À quelle fréquence le collier envoie les données ? (toutes les X secondes/minutes)

---

## 5) ML / IA (optionnel pour la démo)
16. Voulez-vous montrer une IA dans la démo ? (oui/non)
17. Si oui : quelle IA vous montrez ? (ex : repérer un choc, reconnaître un type d'événement, etc.)
18. D'où viennent les données IA ? (capteurs réels, simulation, données déjà existantes)
19. Comment vous prouvez que l'IA marche, rapidement ? (ex : nombre de réussites sur 10 tests)
20. Décrivez le fonctionnement IA en 3 lignes simples :
   - entrée (données)
   - résultat (score/score)
   - décision (si score > X alors alerte)

---

## 6) Traçabilité / preuve que personne ne triche (sans se bloquer sur la blockchain)
21. Pour chaque alerte, vous stockez quoi exactement ? (liste de 4-6 infos max)
22. Comment vous garantissez que l'historique ne change pas facilement ?
   (ex : “journal ajouté et signé”, ou “hash chain” si vous connaissez)
23. Qui voit le journal ? Et comment vous exportez pour le jury (CSV/PDF) ?
24. Comment vous montrez au jury que l’historique est “intègre” ? (ex : afficher un résumé + horodatage)

---

## 7) Sécurité : éviter la copie d’un ID
25. Comment vous identifiez le mineur ? (ID, QR du collier, badge)
26. Comment empêcher qu’une autre personne copie l’ID ? (une méthode simple côté serveur)
27. Et si pas de réseau ? (stockage local + envoi plus tard, ou alerte sur place)
28. Quelles données doivent rester privées ? (ne pas afficher des infos personnelles)

---

## 8) Ce que vous montrez sur le tableau de bord (jury)
29. Quelles 4 vues allez-vous afficher ? (ex : liste alertes, détails, carte simple, export)
30. Quels indicateurs vous donnez au jury ? (nb alertes, temps avant alerte, faux positifs estimés)
31. Quel message d’alerte clair vous affichez ? (ex : “Zone interdite détectée - suspect” + date/heure + ID)

---

## 9) Validation terrain (même avec simulation au début)
32. Combien de scénarios testez-vous avant le concours ? (ex : 10)
33. Pour chaque scénario : attendu vs résultat réel
34. Quelles erreurs fréquentes vous devez éviter ? (GPS instable, pas de réseau, capteurs bruités)

---

## 10) Plan 4-5 jours (check rapide)
35. Jour 1 : capteurs (ou simulation) + format données (JSON) + endpoint serveur
36. Jour 2 : règles de détection (zone + déclenchement) + création d’alerte + preuve d’intégrité
37. Jour 3 : dashboard + chronologie + export
38. Jour 4 : ajouter (optionnel) IA ou améliorer la détection pour réduire les erreurs
39. Jour 5 : préparer la démo finale + tests + explications simples

---

## À compléter (zone de saisie équipe)
- Événement 1 :
- Événement 2 :
- Règle évènement 1 (valeur + durée) :
- Règle évènement 2 (valeur + durée) :
- Zone interdite (comment vous la définissez) :
- Capteurs retenus :
- Traçabilité (méthode simple) :
- IA (oui/non + idée + seuil si besoin) :
- Scénario démo final (5 étapes) :
