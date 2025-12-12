import os
from flask import Flask
from api_utilisateur.setting.config import db

from api_utilisateur.blueprints.crud_utilisateur.create_user import create_user_bp
from api_utilisateur.blueprints.crud_utilisateur.delete_user import delete_user_bp
from api_utilisateur.blueprints.crud_utilisateur.get_user import get_user_bp
from api_utilisateur.blueprints.crud_utilisateur.update_user import update_user_bp

from api_utilisateur.blueprints.crud_complete_account.complete_compte import complete_compte_bp
from api_utilisateur.blueprints.crud_log_in.log_in import log_in_bp

from api_utilisateur.blueprints.crud_product.add_product import add_product_bp
from api_utilisateur.blueprints.crud_product.delete_product import delete_product_bp
from api_utilisateur.blueprints.crud_product.update_product import update_product_bp
from api_utilisateur.blueprints.crud_product.get_product import get_product_bp

from api_utilisateur.blueprints.crud_shop.add_shop import add_shop_bp

from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from api_utilisateur.extensios.cors import init_cors
from api_utilisateur.extensios.logging import init_logging
from api_utilisateur.extensios.limiter import init_limiter


migrate = Migrate()

load_dotenv()

def create_app():
    my_app = Flask(__name__)
    my_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    my_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    my_app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    my_app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    my_app.config["JWT_ALGORITHM"] = os.environ.get('JWT_ALGORITHM')
    my_app.config["JWT_ALGORITHM_HPW"] = os.environ.get('JWT_ALGORITHM_HPW')
    my_app.config['JWT_EXP_DELTA_SECONDS'] = int(os.environ.get('JWT_EXP_DELTA_SECONDS'))
    # my_app.config['PORT'] = int(os.environ.get("PORT"))

    db.init_app(my_app)
    jwt = JWTManager(my_app)
    migrate.init_app(my_app, db)
    init_cors(my_app)
    init_logging(my_app)
    init_limiter(my_app)


    # routes user
    my_app.register_blueprint(create_user_bp)
    my_app.register_blueprint(delete_user_bp)
    my_app.register_blueprint(get_user_bp)
    my_app.register_blueprint(update_user_bp)

    # Complete compte
    my_app.register_blueprint(complete_compte_bp)

    # routes Shop
    my_app.register_blueprint(add_shop_bp)

    # routes product
    my_app.register_blueprint(add_product_bp)
    my_app.register_blueprint(get_product_bp)

    # login
    my_app.register_blueprint(log_in_bp)



    return my_app

# for gunicorn
app = create_app()

@app.route("/deployment_metrics")
def metrics():
    return {
        "uptime": "OK",
        "database": "connected",
        "version": "1.0.0"}, 200



@app.route("/migrate/seed")
def migrate_seed():
    from api_utilisateur.seed import seed, run_migrations
    try:
        run_migrations()
        seed()
        return "Database seeded", 200
    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))