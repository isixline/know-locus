from flask import Blueprint, jsonify, request
from core.match import match_in_know_lib
from utils.vector_cacher import clear_vector_cache
from core.filter import idea_notes_filter

matcher_bp = Blueprint("matcher", __name__, url_prefix="/matcher")


@matcher_bp.route("/idea", methods=["POST"])
def search_idea():
    data = request.get_json()
    query = data.get("query", "")
    top = data.get("top", 10)
    results = match_in_know_lib(query, idea_notes_filter, top)
    return jsonify({"results": results})


@matcher_bp.route("/cache/vector", methods=["DELETE"])
def clear_cache_vector():
    clear_vector_cache()
    return jsonify({"message": "Vector cache cleared successfully."})
