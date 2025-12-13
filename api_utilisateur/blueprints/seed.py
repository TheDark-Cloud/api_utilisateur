from flask import Blueprint, jsonify

from api_utilisateur.model_db import db, Role, Categorie

seed_bp = Blueprint("seed", __name__)

@seed_bp.route("/migrate-seed", methods=["POST"])
def migrate_and_seed():

    try:


            # 2. Seed roles
            roles = ['admin', 'vendeur', 'client', 'restaurateur', 'artisan']
            for r in roles:
                if not Role.query.filter_by(name_role=r).first():
                    db.session.add(Role(name_role=r))

            db.session.commit()

            return jsonify({
                "message": "Migrations and seeding completed successfully"
            }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
