API Utilisateur – Flask + PostgreSQL + Railway

Cette API est une application Flask modulaire basée sur un pattern Application Factory.  
Elle gère l’authentification, la gestion des utilisateurs, des produits, des shops et la complétion de compte.  
Le projet est conçu pour être déployé facilement sur Railway.

------------------------------------------------------------
FONCTIONNALITÉS
------------------------------------------------------------

- Création, suppression, mise à jour et récupération d’utilisateurs
- Authentification JWT
- Gestion des shops
- Gestion des produits
- Complétion de compte
- Base de données PostgreSQL
- Migrations via Flask-Migrate
- Architecture modulaire avec Blueprints

------------------------------------------------------------
STRUCTURE DU PROJET
------------------------------------------------------------

api_utilisateur/
    app.py
    model_db.py
    requirements.txt
    Procfile
    README.mdr
    migrations/
    blueprints/
        crud_admin
        crud_utilisateur/
        crud_product/
        crud_role/
        crud_shop/
        crud_log_in/
        crud_complete_account/
    setting/
        __init__.py
        config.py
        auth.py
        tokenize
    tests/
    .venv/

------------------------------------------------------------
CONFIGURATION DE L’APPLICATION
------------------------------------------------------------

L’application utilise une fonction create_app() pour :

- Charger les variables d’environnement
- Initialiser SQLAlchemy
- Initialiser JWT
- Initialiser Flask-Migrate
- Enregistrer les blueprints

Le serveur démarre avec :

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

Compatible Railway et local.

------------------------------------------------------------
VARIABLES D’ENVIRONNEMENT (RAILWAY)
------------------------------------------------------------

À ajouter dans Railway → Variables :

SQLALCHEMY_DATABASE_URI_API_UTILISATEUR=postgres://...
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=...
JWT_SECRET_KEY=...
JWT_ALGORITHM=HS256
JWT_ALGORITHM_HPW=HS512
JWT_EXP_DELTA_SECONDS=...

Railway fournit automatiquement :
PORT

------------------------------------------------------------
INSTALLATION LOCALE
------------------------------------------------------------

1. Cloner le projet :
git clone <url-du-repo>
cd api_utilisateur

2. Créer un environnement virtuel :
python -m venv .venv
source .venv/bin/activate (Linux/Mac)
.venv\Scripts\activate (Windows)

3. Installer les dépendances :
pip install -r requirements.txt

4. Lancer l’application :
python app.py

------------------------------------------------------------
REQUIREMENTS.TXT
------------------------------------------------------------

Flask
Flask-JWT-Extended
Flask-Migrate
Flask-SQLAlchemy
python-dotenv
gunicorn
psycopg2-binary

------------------------------------------------------------
PROCFILE
------------------------------------------------------------

web: gunicorn "app:create_app()"

------------------------------------------------------------
MIGRATIONS
------------------------------------------------------------

Local :
flask db init
flask db migrate -m "pre deployment migration"
flask db upgrade

Production Railway :
railway run flask db upgrade

------------------------------------------------------------
DÉPLOIEMENT SUR RAILWAY
------------------------------------------------------------

1. Railway → New → Deploy Service → GitHub Repo
2. Railway détecte Python automatiquement
3. Railway lit requirements.txt et Procfile
4. Ajouter les variables d’environnement
5. Déployer

------------------------------------------------------------
VÉRIFICATION
------------------------------------------------------------

Railway fournit une URL publique :
https://<nom-du-service>.up.railway.app

Tester :
GET /user/get
POST /user/create
POST /login

------------------------------------------------------------
BONNES PRATIQUES
------------------------------------------------------------

- Utiliser Gunicorn en production
- Ne jamais exposer les clés dans GitHub
- Utiliser les migrations pour la base
- Garder les blueprints modulaires
- Ajouter des logs pour la production

------------------------------------------------------------
FIN DU README
------------------------------------------------------------

---

Si tu veux, je peux aussi te générer une version **README.md** et une version **README.txt** séparées, ou même un **template pour la documentation API (Swagger/OpenAPI)**.
