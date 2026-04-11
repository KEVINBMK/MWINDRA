## MWINDRA — Système intelligent de sécurité minière (MVP)

Dépôt de **cadrage et de spécification** pour le MVP logiciel (bracelet → API → tableau de bord).

---

### Fichier principal

| Fichier | Rôle |
|--------|------|
| [`SPEC_MVP_LOGICIEL_MWINDRA.md`](SPEC_MVP_LOGICIEL_MWINDRA.md) | Spécification complète : questions d’accord, architecture, données, API, écrans, plan 4–5 jours, tests. |
| [`EXPLICATION_SIMPLE_SPEC_MVP.md`](EXPLICATION_SIMPLE_SPEC_MVP.md) | Version simplifiée de la spec (lecture rapide pour toute l’équipe). |
| [`ORGANIGRAMME_UTILISATEURS.md`](ORGANIGRAMME_UTILISATEURS.md) | Organigramme des rôles (terrain vs plateforme SaaS). |
| [`DIAGRAMMES_MVP_PRE_DEV.md`](DIAGRAMMES_MVP_PRE_DEV.md) | Diagrammes de séquences, contexte, états, ER — avant développement. |

---

### Comment utiliser `SPEC_MVP_LOGICIEL_MWINDRA.md`

1. **Ouvrir le fichier** (sur GitHub ou en local) et lire d’abord l’introduction + **« Comment utiliser ce document »** en haut.
2. **Remplir / décider la section 1** (utilisateur demo, internet, GPS, alertes, seuils radiation, confidentialité). Sans ces choix, le développement part dans tous les sens.
3. **Aligner l’équipe** : soit vous recopiez les décisions dans le fichier (édition + commit), soit vous utilisez l’issue ci-dessous pour **cocher** les options.
4. **Développement** : les sections **2 à 7** décrivent ce qu’il faut coder (contrat JSON, endpoints, 3 pages du dashboard). Les sections **8 à 13** précisent les options et le calendrier.
5. **Avant la présentation** : vérifier la **Definition of Done** (fin du fichier spec).

---

### Décisions à cocher sur GitHub (cases interactives)

Dans un fichier `.md` du dépôt, les cases ne s’enregistrent en général **pas** au clic. Pour travailler ensemble avec des **cases cliquables** :

- [Créer une issue « Décisions MVP »](https://github.com/KEVINBMK/MWINDRA/issues/new?template=decisions-mvp.md) → **Submit** → puis cocher dans la description de l’issue.

Le modèle d’issue est dans [`.github/ISSUE_TEMPLATE/decisions-mvp.md`](.github/ISSUE_TEMPLATE/decisions-mvp.md).

---

### Structure du dépôt

```
MWINDRA/
  README.md                          ← vous êtes ici
  SPEC_MVP_LOGICIEL_MWINDRA.md       ← spec détaillée (référence)
  EXPLICATION_SIMPLE_SPEC_MVP.md     ← résumé simple
  ORGANIGRAMME_UTILISATEURS.md       ← rôles utilisateurs
  DIAGRAMMES_MVP_PRE_DEV.md          ← séquences + états + ER
  .github/ISSUE_TEMPLATE/
    decisions-mvp.md                 ← modèle d’issue (décisions)
```
