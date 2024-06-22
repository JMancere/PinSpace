from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix="/api/user")

@bp.route("/")
def index():
    return "Here's user route in PinSpace!"
