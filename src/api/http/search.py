from flask import Flask, request, jsonify
from core.search import search_files_in_know_lib
from core.filter import inspiration_notes_filter
from utils.vector_cacher import clear_vector_cache

app = Flask(__name__)


@app.route('/search/inspiration', methods=['POST'])
def search_inspiration():
    data = request.get_json()
    query = data.get('query', '')
    top = data.get('top', 10)
    results = search_files_in_know_lib(query, inspiration_notes_filter, top)
    return jsonify({'results': results})

@app.route('/cache/vector', methods=['DELETE'])
def clear_cache_vector():
    clear_vector_cache()
    return jsonify({'message': 'Vector cache cleared successfully.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
