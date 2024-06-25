from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix="/api/auth")

@bp.route("/")
def index():
    return "Here's user route in PinSpace!"
