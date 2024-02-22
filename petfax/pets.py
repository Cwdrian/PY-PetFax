from flask import Blueprint

bp = Blueprint(
    "pets",
    __name__,
    url_prefix="/pets"
)
@bp.route("/")
def pets():
    return "these are my pets for adopt"