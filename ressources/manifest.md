# Manifeste du Projet : ELYORA
**Version :** 2.0 (Basée sur l'implémentation réelle)
**Contexte Académique :** EHEI Oujda, Filière Génie Informatique (2025-2026).
**Équipe :** Salah-Eddine El-Ghazi, Ayoube Arabat, Hamza Chdaoui.

## 1. Description du Projet
Elyora est une plateforme intelligente de tourisme local. Elle génère des itinéraires personnalisés et permet la réservation globale d'expériences touristiques (hôtels, restaurants, activités, transports). 

## 2. Architecture Tri-Technologique (Base partagée MySQL)
1. **Module Web (Client / Touriste) :** Développé en PHP 8+ (POO, PDO), HTML5, CSS3, JS Vanilla.
2. **Module Opérations (Admin C++) :** Gère l'inventaire en mémoire (Vecteurs STL, `Structs.h`).
3. **Module Rapports (Admin Java) :** Gère l'analyse des réservations et statistiques (Export CSV).

## 3. Configuration et Sécurité Globale
- **Connexion BDD (`config.php`) :** Utilisation stricte de `PDO`. Les exceptions sont activées (`PDO::ERRMODE_EXCEPTION`) et les résultats sont formatés en tableaux associatifs (`PDO::FETCH_ASSOC`).
- **Sessions :** L'état global est maintenu par les sessions PHP (`session_start()`).