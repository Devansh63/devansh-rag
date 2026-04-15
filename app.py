"""
Flask web application for the Devansh RAG chatbot.

Endpoints:
  GET  /           → Serve the main chat UI (templates/index.html)
  POST /api/chat   → {"message": "..."} → {"response": "...", "sources": [...]}
  POST /api/suggest → {} → {"questions": [...]}

Run with:
    python app.py
or in production:
    gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 120 app:app
"""

import os
import sys

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

_allowed_origin = os.environ.get("ALLOWED_ORIGIN", "*")
CORS(app, resources={r"/api/*": {"origins": _allowed_origin}})

_rate_limit = os.environ.get("RATE_LIMIT", "20 per minute")
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[_rate_limit],
    storage_uri="memory://",
)

_pipeline = None


def get_pipeline():
    """Lazily initialize and return the singleton RAGPipeline."""
    global _pipeline
    if _pipeline is None:
        from rag.pipeline import RAGPipeline
        chroma_path = os.path.join(os.path.dirname(__file__), "chroma_db")
        _pipeline = RAGPipeline(chroma_path=chroma_path)
    return _pipeline


def _check_env():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(
            "ERROR: GEMINI_API_KEY environment variable is not set.\n"
            "  Add it to your .env file or export it in your shell.",
            file=sys.stderr,
        )
        sys.exit(1)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
@limiter.limit("10 per minute")
def chat():
    try:
        data = request.get_json(force=True, silent=True)
        if not data or "message" not in data:
            return jsonify({"error": "Request body must include a 'message' field."}), 400

        message = data["message"].strip()
        if not message:
            return jsonify({"error": "Message cannot be empty."}), 400
        if len(message) > 2000:
            return jsonify({"error": "Message is too long (max 2000 characters)."}), 400

        pipeline = get_pipeline()
        result = pipeline.chat(message)
        return jsonify({"response": result["response"], "sources": result["sources"]})

    except ValueError as e:
        app.logger.error("Configuration error: %s", str(e))
        return jsonify({"error": "Server configuration error. Check the API key."}), 500
    except Exception as e:
        app.logger.error("Error processing chat request: %s", str(e))
        return jsonify({"error": "An unexpected error occurred. Please try again."}), 500


@app.route("/api/suggest", methods=["POST"])
def suggest():
    questions = [
        "Where did you grow up?",
        "What are you studying at UIUC?",
        "Tell me about the NeuroDrone project",
        "What did you build at OPEXUS?",
        "What ML research have you done?",
        "What are your technical skills?",
    ]
    return jsonify({"questions": questions})


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "devansh-rag"})


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed."}), 405

@app.errorhandler(429)
def rate_limited(e):
    return jsonify({"error": "Too many requests. Please wait a moment before trying again."}), 429

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error."}), 500


if __name__ == "__main__":
    _check_env()
    print("Initializing RAG pipeline...")
    try:
        get_pipeline()
        print("RAG pipeline ready.")
    except Exception as exc:
        print(f"WARNING: Could not initialize pipeline at startup: {exc}")
        print("Make sure you have run: python ingest.py")

    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Flask app on http://0.0.0.0:{port}  (debug={debug})")
    app.run(host="0.0.0.0", port=port, debug=debug)
