# Explication tres simple — SPEC MVP logiciel MWINDRA

Ce fichier dit la meme chose que `SPEC_MVP_LOGICIEL_MWINDRA.md`, mais avec des mots simples.

---

## En une phrase

Les questions du spec servent a **se mettre d’accord avant de coder**.  
Sinon chacun imagine une autre demo.

---

## Les questions de la section 1 (une par une)

### 1. Qui utilise l’ecran pendant la demo ?

**Pour quoi ?** Savoir **pour qui** on fait le site.  
**Objectif en 1 phrase :** en 2 minutes, qu’est-ce qu’on veut montrer ?  
**Les 5 etapes :** le petit film de la demo, du debut a la fin (qui clique ou, qu’on voit quoi).

---

### 2. Quelles alertes au debut (MVP) ?

**Pour quoi ?** Savoir ce qui doit **crier tout de suite** sur l’ecran.  
Ici : **radiation** (couleurs) et **SOS** (bouton urgence).  
Le reste = **apres** la premiere version.

**Jaune :** alerte forte ou juste un petit avertissement ? Il faut choisir.

---

### 3. Internet pendant la demo ?

**Pour quoi ?** Le bracelet et le site doivent **parler ensemble**.  
Si le reseau est mauvais, la demo peut planter.

**Plan B :** si internet coupe, on fait quoi ? (autre reseau, pas de carte, donnees de test sur un PC, etc.)

---

### 4. Position : GPS ou pas ? Affichage ?

**Pour quoi ?** Montrer **ou** est la personne.

- **Carte** = souvent joli, souvent besoin d’internet.
- **Texte (chiffres lat/lng)** = moins joli, souvent **plus sur** pour la demo.

---

### 5. Seuils radiation (vert / jaune / rouge)

**Pour quoi ?** Des **nombres fixes** : a partir de quand c’est vert, jaune, rouge.  
Meme si le capteur est **simule**, on garde **les memes regles** pour tout le monde.

---

### 6. Identifiants et confidentialite

**Pour quoi ?** Comment on nomme le bracelet (ex. BR-001) et **si on affiche des noms**.

Souvent on affiche **seulement le numero du bracelet**, pas le nom des personnes — **plus simple et plus sur** pour la vie privee.

---

## Autres choix plus loin dans le spec (tres court)


| Sujet                               | En simple                                                                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Qui decide vert/jaune/rouge ?       | Souvent le **serveur** = une seule regle pour tous.                                                     |
| Site et programme au meme endroit ? | Au debut **oui** = plus facile a installer.                                                             |
| Email / Telegram en plus ?          | **Optionnel** ; souvent l’**ecran suffit** au MVP.                                                      |
| Chaine de hash (preuve)             | **Option** pour expliquer au jury que l’historique est difficile a trafiquer. Pas obligatoire au debut. |


---

*Pour le detail technique (API, pages, planning), voir `SPEC_MVP_LOGICIEL_MWINDRA.md`.*