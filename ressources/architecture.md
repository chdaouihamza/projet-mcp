# Architecture Technique et Normes - ELYORA

## 1. Module Web (PHP)
- **Modèle de fichier type :** Toute la logique PHP (traitements, requêtes) doit être placée **au sommet** du fichier, suivie du code HTML.
- **Sécurité SQL :** Interdiction absolue d'utiliser `mysqli` ou de concaténer des variables dans le SQL. Utilisation exclusive de requêtes préparées : `$stmt = $pdo->prepare(); $stmt->execute([$var]);`.
- **Authentification (`register.php`) :** Les mots de passe doivent faire au minimum 8 caractères et être hachés avec la fonction native `password_hash($password, PASSWORD_DEFAULT)`.

## 2. Module Rapports (Java)
- **Dépendance :** Le projet requiert le driver `mysql-connector-j-8.3.0.jar`.
- **Packages :** - `src/model/` : Entités de données (`RapportReservation.java`, etc.).
  - `src/database/` : Gère la connexion Singleton (`Database.java`).
  - `src/service/` : Contient toute la logique métier (`StatistiquesService.java`).
  - `src/view/` : Affichage console, strictement aucune requête SQL ici (`MenuAdmin.java`).

## 3. Module Opérations (C++)
- Utilisation des références (`&`) pour le passage d'arguments et interdiction des pointeurs bruts si non justifiés. Pas de bibliothèques tierces, uniquement le standard C++.