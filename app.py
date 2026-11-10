
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({
        "status": "ok"
    }), 200


@app.post("/api/sum")
def sum_numbers():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Se esperaba un objeto JSON"
        }), 400

    if "a" not in data or "b" not in data:
        return jsonify({
            "error": "Faltan los parámetros a o b"
        }), 400

    a = data["a"]
    b = data["b"]

    if (
        isinstance(a, bool)
        or isinstance(b, bool)
        or not isinstance(a, (int, float))
        or not isinstance(b, (int, float))
    ):
        return jsonify({
            "error": "Los parámetros deben ser números"
        }), 400

    return jsonify({
        "result": a + b
    }), 200


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=False
    )
