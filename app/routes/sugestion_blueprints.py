from flask import Blueprint
from app.controllers.sugestion_controllers import delete_sugestion, get_all_sugestion, register_sugestion, delete_sugestion


bp_sugestions = Blueprint('bp_sugestions', __name__)


bp_sugestions.post("/sugestions")(register_sugestion)
bp_sugestions.get("/sugestions")(get_all_sugestion)
bp_sugestions.delete("/sugestions")(delete_sugestion)

