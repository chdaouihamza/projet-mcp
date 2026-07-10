# Dictionnaire de Données - ELYORA (SGBDR: MySQL)
**Nom de la base :** `agence_voyage`

## 1. Tables Utilisateurs et Profil
- **touriste** : `id_touriste` (PK), `nom`, `prenom`, `email` (UNIQUE), `motDePasse`, `telephone`.
- **sejour** : Profil voyageur. Lié au touriste (`ON DELETE CASCADE`). Contient `budget`, `dureeSejour`, `centresInteret` (stockés sous forme de chaîne, ex: "Nature,Art"), `modeTransportPrefere`.

## 2. Table Centrale : Reservation
Table regroupant toutes les transactions.
- **Colonnes :** `id_reservation` (PK), `date_debut`, `date_fin`, `statut`.
- **Clés Étrangères (Contraintes de suppression) :**
  - Liée à `touriste` : `ON DELETE CASCADE` (Si le touriste est supprimé, la réservation disparaît).
  - Liées aux services (`hotel`, `restaurant`, `activite`, `transport`) : `ON DELETE SET NULL` (Pour garder l'historique financier même si l'hôtel ferme).

## 3. Tables de Services (Catalogue)
- `hotel` et `chambre` (ON DELETE CASCADE entre hôtel et chambre).
- `restaurant` et `plat`.
- `activite`, `lieutouristique`, `guidetouristique`, `transport`.

## 4. Tables de Planification
- `itineraire` (PK `id_itineraire`).
- Tables de liaison Many-to-Many : `itineraire_lieutouristique` et `itineraire_transport`.