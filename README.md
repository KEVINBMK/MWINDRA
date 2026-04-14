## MWINDRA — Système intelligent de sécurité minière (MVP)

Dépôt de **cadrage et de spécification** pour le MVP logiciel (bracelet → API → tableau de bord).

---

### Fichier principal

| Fichier | Rôle |
|--------|------|
| [`docs/`](docs/) | **Documentation MVP** (spec, organigramme, diagrammes) — index : [`docs/README.md`](docs/README.md). |
| [`simulation/README.md`](simulation/README.md) | **Démo jury** : API + pages bracelet / superviseur / 3D (tout simulé). |

Les fichiers détaillés sont dans **`docs/`** : [`SPEC_MVP_LOGICIEL_MWINDRA.md`](docs/SPEC_MVP_LOGICIEL_MWINDRA.md), [`EXPLICATION_SIMPLE_SPEC_MVP.md`](docs/EXPLICATION_SIMPLE_SPEC_MVP.md), [`ORGANIGRAMME_UTILISATEURS.md`](docs/ORGANIGRAMME_UTILISATEURS.md), [`DIAGRAMMES_MVP_PRE_DEV.md`](docs/DIAGRAMMES_MVP_PRE_DEV.md).

---

### Comment utiliser `docs/SPEC_MVP_LOGICIEL_MWINDRA.md`

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
  docs/                              ← documentation MVP (2D : spec, organigramme, diagrammes)
    README.md
    SPEC_MVP_LOGICIEL_MWINDRA.md
    EXPLICATION_SIMPLE_SPEC_MVP.md
    ORGANIGRAMME_UTILISATEURS.md
    DIAGRAMMES_MVP_PRE_DEV.md
  simulation/                        ← démo jury (API + pages web + 3D)
  .github/ISSUE_TEMPLATE/
    decisions-mvp.md                 ← modèle d’issue (décisions)
```
