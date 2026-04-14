# MWINDRA — Organigramme des utilisateurs du système

Ce schéma décrit **qui utilise quoi** : bracelet (terrain) vs plateforme **SaaS** (supervision). À adapter selon votre organisation réelle.

---

## Vue hiérarchique (Mermaid)

> Affichage : GitHub affiche le diagramme ; sinon copier le bloc dans [mermaid.live](https://mermaid.live).

```mermaid
flowchart TB
  subgraph Strategique["Niveau stratégique"]
    DIR["Direction / QHSE"]
  end

  subgraph Plateforme["Plateforme MWINDRA — SaaS"]
    RS["Responsable sécurité"]
    SUP["Superviseur de zone / chef de poste"]
    INS["Inspecteur / contrôle"]
    RH["RH — rapports & suivi"]
  end

  subgraph Technique["Support technique"]
    ADM["Administrateur système / IT"]
  end

  subgraph Terrain["Terrain — dispositif porté"]
    MIN["Mineur / technicien — porteur du bracelet"]
  end

  DIR --> RS
  RS --> SUP
  SUP --> MIN
  INS -.->|"consultation / export"| RS
  RH -.->|"tableaux & historique"| RS
  ADM -.->|"comptes, accès, infra"| RS
  ADM -.-> SUP
```

**Lecture rapide**

- **Flèche pleine** : chaîne opérationnelle classique (décision → terrain).
- **Flègle pointillée** : accès transversal (contrôle, RH, IT).

---

## Rôles et usage (résumé)

| Rôle | Utilise surtout | Rôle dans MWINDRA |
|------|-----------------|-------------------|
| **Porteur du bracelet** | Bracelet IoT | Mesures, alertes locales, SOS |
| **Superviseur** | SaaS (dashboard) | Voir alertes en temps réel, détails, statuts |
| **Responsable sécurité** | SaaS | Supervision globale, validation incidents, procédures |
| **Inspecteur** | SaaS (lecture) | Contrôle, exports, preuves |
| **Direction / QHSE** | SaaS (synthèses) | Indicateurs, décisions stratégiques |
| **RH** | SaaS (option / phase 2) | Bilan incidents, lien formation / dossiers |
| **Admin IT** | Console admin / infra | Comptes, sauvegardes, disponibilité |

---

## Version texte (si pas de rendu Mermaid)

```
                    Direction / QHSE
                            |
                Responsable sécurité
                     /            \
         Superviseur de zone    Inspecteur
                |
         Porteur du bracelet
    (mineur / technicien)

    RH --------------> (accès rapports, phase 2)
    Admin IT --------> (comptes & infrastructure)
```

---

## Note pour la présentation jury

- **Utilisateur principal SaaS** : superviseur + responsable sécurité (alertes immédiates).  
- **Utilisateur principal terrain** : porteur du bracelet.  
- **RH et Direction** : utiles pour le **modèle économique** et la **gouvernance**, souvent en **consultation** ou **phase 2** pour ne pas surcharger le MVP.
