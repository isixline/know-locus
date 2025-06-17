from flask import Flask, request, jsonify
from core.search import search_files_in_know_lib
from utils.vector_cacher import clear_vector_cache
from core.parser import parse_md
from config.env import get_know_lib_path
from core.filter import tech_notes_filter
from core.filter import idea_notes_filter
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/search/idea", methods=["POST"])
def search_idea():
    data = request.get_json()
    query = data.get("query", "")
    top = data.get("top", 10)
    results = search_files_in_know_lib(query, idea_notes_filter, top)
    return jsonify({"results": results})


@app.route("/cache/vector", methods=["DELETE"])
def clear_cache_vector():
    clear_vector_cache()
    return jsonify({"message": "Vector cache cleared successfully."})


@app.route("/nodes/idea", methods=["GET"])
def get_idea_nodes():
    know_lib = parse_md(get_know_lib_path(), idea_notes_filter)
    return jsonify({"nodes": know_lib})

@app.route("/nodes/tech", methods=["GET"])
def get_nodes_tech():
    know_lib = parse_md(get_know_lib_path(), tech_notes_filter)
    return jsonify({"nodes": know_lib})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
