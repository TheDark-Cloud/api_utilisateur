from flask import jsonify
from flask_migrate import upgrade

from api_utilisateur.app import create_app
from api_utilisateur.model_db import db, Role, Categorie

def seed():
    app = create_app()

    with app.app_context():
        # Insert roles
        roles = ['admin', 'vendeur', 'client', 'restaurateur', 'artisan']
        for r in roles:
            if not Role.query.filter_by(name_role=r).first():
                db.session.add(Role(name_role=r))

        # Insert categories
        product_types = [
            "Electronics",
            "Fashion & Apparel",
            "Food & Beverages",
            "Home & Furniture",
            "Beauty & Personal Care"
        ]
        for c in product_types:
            if not Categorie.query.filter_by(categorie_name=c).first():
                db.session.add(Categorie(categorie_name=c))

        db.session.commit()
        print("Seed completed successfully")

def run_migrations():
    try:
        # Run migrations
        upgrade()
        return jsonify({"message": "Migrations applied successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    seed()
