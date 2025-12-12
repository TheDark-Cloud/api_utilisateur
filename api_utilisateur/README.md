# API Utilisateur – Flask + PostgreSQL + Render

## Description
API Flask modulaire avec authentification JWT, gestion utilisateurs, produits, shops, complétion de compte, migrations et PostgreSQL. Déployée sur Render avec Gunicorn.

## Fonctionnalités
- Authentification JWT
- CRUD Utilisateurs
- CRUD Produits
- CRUD Shops
- Complétion de compte
- PostgreSQL + SQLAlchemy
- Migrations Flask-Migrate
- CORS, Logging, Rate Limiting
- Routes système (home, metrics, seed)

## Structure du projet
api_utilisateur/
    api_utilisateur/
        app.py
        model_db.py
        migrations/
        blueprints/
        routes/
            home.py
            health.py
            metrics.py
            seed.py
        extensions/
            logging.py
            cors.py
            limiter.py
            swagger.py
        setting/
            config.py
            auth.py
        requirements.txt
        Procfile

## Routes système
GET /              → Homepage  
GET /health        → Health check  
GET /metrics       → Monitoring  
GET /seed          → Seed database (à utiliser une seule fois)

## Variables d’environnement (Render)
DATABASE_URL=postgresql://user:password@host:5432/dbname  
SECRET_KEY=...  
JWT_SECRET_KEY=...  
JWT_ALGORITHM=HS256  
JWT_ALGORITHM_HPW=HS512  
JWT_EXP_DELTA_SECONDS=3600  
SQLALCHEMY_TRACK_MODIFICATIONS=False  

Render fournit automatiquement : PORT

## Installation locale
git clone <repo>  
cd api_utilisateur  
python -m venv .venv  
source .venv/bin/activate  (Linux/Mac)  
.venv\Scripts\activate     (Windows)  
pip install -r requirements.txt  
python app.py  

## Requirements.txt
Flask  
Flask-JWT-Extended  
Flask-Migrate  
Flask-SQLAlchemy  
python-dotenv  
gunicorn  
psycopg2-binary  
flask-cors  
flask-limiter  
flasgger  

## Procfile (Render)
web: gunicorn api_utilisateur.app:app

## Migrations
Local :  
flask db init  
flask db migrate -m "initial"  
flask db upgrade  

Render (Shell) :  
flask db upgrade  

## Déploiement Render
1. Render → New Web Service → Connect GitHub  
2. Render détecte Python automatiquement  
3. Ajouter les variables d’environnement  
4. Déployer  





# ROUTES – CRUD LOGIC (UTILISATEURS, PRODUITS, SHOPS, ROLES, AUTH)


## AUTHENTIFICATION

POST /user/login

============================================================

## UTILISATEURS (crud_utilisateur)


POST   /utilisateur/create_user

GET    /utilisateur/get_user

PUT    /utilisateur/update_user

DELETE /utilisateur/delete_user

============================================================
## ADMIN (crud_admin)


GET    /
GET    /
PUT    /
DELETE /

============================================================
## ROLES (crud_role)

POST   /role/add_role

GET    /role/get_role


============================================================
## PRODUITS (crud_product)

POST   /product/add_product

GET    /product/get_product


============================================================
## SHOPS (crud_shop)

POST   /vendeur/add_shop

============================================================
## COMPLETION DE COMPTE (crud_complete_account)

POST /complete-account

============================================================
## ROUTES SYSTEME

To be implemented

============================================================
## AUTH HEADERS

Toutes les routes protégées utilisent :

Authorization: Bearer <token>
