from flask import Blueprint, jsonify, request
from core.match import match_in_know_lib
from core.filter import idea_notes_filter

matcher_bp = Blueprint("matcher", __name__, url_prefix="/matcher")


@matcher_bp.route("/idea", methods=["POST"])
def search_idea():
    data = request.get_json()
    query = data.get("query", "")
    top = data.get("top", 10)
    results = match_in_know_lib(query, idea_notes_filter, top)
    return jsonify({"results": results})

