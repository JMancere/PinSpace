'''Starting point for PinSpace'''
from flask import Flask, render_template, redirect
# from flask_migrate import Migrate
from .config import Configuration
from .models import db
from .routes import root, user

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(root.bp)
app.register_blueprint(user.bp)
db.init_app(app)  # Configure the application with SQLAlchemy
# Migrate(app, db)
