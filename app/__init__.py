from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Ini
from config import Config

# Ini error???
#     from flask_sqlalchemy import SQLAlchemy
# ModuleNotFoundError: No module named 'flask_sqlalchemy'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .models import models
    with app.app_context():
        db.create_all()
        if not models.Category.query.first():
            db.session.add_all([
                models.Category(name="transportasi"),
                models.Category(name="pangan"),
                models.Category(name="energi")
            ])
            db.session.commit()

    # from app.controllers.product_controller import product_bp
    # from app.controllers.category_controller import category_bp
    from app.controllers import category_bp,product_bp
    app.register_blueprint(product_bp)
    app.register_blueprint(category_bp)

    return app
