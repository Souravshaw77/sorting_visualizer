from flask import Flask, render_template, request, jsonify
import random

# Import sorting algorithms
from algorithms.bubble import bubble_sort
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
from algorithms.merge import merge_sort
from algorithms.quick import quick_sort
from algorithms.heap import heap_sort

app = Flask(__name__)

# Map algorithm names to functions
ALGORITHMS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort
}


# -------------------------------
# Home Route
# -------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -------------------------------
# Generate Random Array
# -------------------------------
@app.route("/api/random")
def generate_random_array():
    try:
        size = int(request.args.get("size", 30))
        size = max(5, min(size, 100))  # safety clamp
        array = [random.randint(10, 300) for _ in range(size)]
        return jsonify(array)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# -------------------------------
# Sort API
# -------------------------------
@app.route("/api/sort", methods=["POST"])
def sort_array():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        algorithm = data.get("algorithm")
        array = data.get("array")

        if algorithm not in ALGORITHMS:
            return jsonify({"error": "Unsupported algorithm"}), 400

        if not isinstance(array, list):
            return jsonify({"error": "Array must be a list"}), 400

        # Run sorting algorithm
        result = ALGORITHMS[algorithm](array)

        return jsonify(result)

    except Exception as e:
        # This helps debugging instead of silently failing
        return jsonify({"error": str(e)}), 500


# -------------------------------
# App Entry Point
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
