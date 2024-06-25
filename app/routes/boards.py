from flask import Blueprint, render_template
from flask_login import login_required
from ..models import Board

bp = Blueprint("boards", __name__, url_prefix="/boards")

@bp.route("/")
@login_required
def index():
    boards = Board.query.all()
    return render_template("boards/index.html", boards=boards)

@bp.route("/ <int:id>")
