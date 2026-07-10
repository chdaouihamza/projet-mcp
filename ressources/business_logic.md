# Règles Métier et Algorithmes - ELYORA

## 1. Algorithme de Tarification (Package Complet)
Le calcul du prix d'un itinéraire complet (`book_full_experience.php`) s'effectue selon la formule stricte suivante :
- **Prix de base :** `(Durée du séjour en jours * 50$) + (Nombre de centres d'intérêts sélectionnés * 5$)`.
- **Taxes :** Une taxe fixe de 10% (`prix * 0.10`) est ajoutée au prix de base pour obtenir le prix total.

## 2. Règles de Profilage (Formulaire `profile.php`)
- **Budget minimum :** Le système doit refuser tout budget inférieur à 50 $.
- **Transport :** Les modes autorisés sont strictement : `Marche`, `Taxi`, `Location`, `Scooter`, `Velos`.

## 3. Règles de Paiement (`payment.php`)
- Le système gère deux modes d'affichage dynamique via JavaScript : `Credit Card` et `PayPal`.
- La validation de la carte bancaire côté client (JS) exige un numéro sans espaces d'au moins 15 caractères et une date d'expiration au format `MM/YY`.