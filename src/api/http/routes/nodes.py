from flask import Blueprint, jsonify
from config.env import get_know_lib_path
from core.parser import parse_md
from core.filter import tech_notes_filter
from core.filter import idea_notes_filter

nodes_bp = Blueprint("nodes", __name__, url_prefix="/nodes")


@nodes_bp.route("/idea", methods=["GET"])
def get_idea_nodes():
    know_lib = parse_md(get_know_lib_path(), idea_notes_filter)
    return jsonify({"nodes": know_lib})


@nodes_bp.route("/tech", methods=["GET"])
def get_nodes_tech():
    know_lib = parse_md(get_know_lib_path(), tech_notes_filter)
    return jsonify({"nodes": know_lib})
