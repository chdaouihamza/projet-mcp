# Charte Graphique et Front-End (Module Web PHP)

## 1. Palette de Couleurs (Extrait de `style.css`)
- **Couleur Primaire (Boutons, Textes forts) :** `#2c6e2f` (Vert foncé).
- **Couleur Secondaire (Header) :** `#F0EBE0` (Beige clair).
- **Fond de page (Body) :** `#faf8f3`.
- **Couleur Accentuation (Éléments culturels) :** `#8b6946` (Marron/Terre).

## 2. Typographie et Formes
- **Police :** `Segoe UI`, Tahoma, Geneva, Verdana, sans-serif.
- **Bordures (Border-Radius) :** Le design Elyora est très arrondi. 
  - Les boutons utilisent `border-radius: 60px;`.
  - Les cartes et conteneurs utilisent `border-radius: 24px;` ou `16px;`.

## 3. JavaScript (`script.js`)
- Le projet n'utilise pas de Framework JS externe.
- Le script gère un message d'accueil dynamique basé sur l'heure du navigateur ("Good morning! 🌿", "Good afternoon! ✨").
- La validation des formulaires se fait via des fonctions Vanilla JS (`validateLoginForm()`, `validateNewProfileForm()`) en utilisant des expressions régulières (Regex) pour les emails et téléphones avant l'envoi au serveur PHP.