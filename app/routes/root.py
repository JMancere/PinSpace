from flask import Blueprint

bp = Blueprint('root', __name__, url_prefix="")

@bp.route("/")
def index():
    return "Here's PinSpace!"
