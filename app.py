"""
Flask server for the Devansh RAG chatbot.

GET  /            serves the chat UI
POST /api/chat    { "message": "..." }  ->  { "response": "...", "sources": [...] }
POST /api/suggest {}                    ->  { "questions": [...] }
GET  /health      simple health check

Run locally:  python app.py
Production:   gunicorn --bind 0.0.0.0:10000 app:app
"""

import os
import sys

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

load_dotenv()

# -- App setup --

app = Flask(__name__)

# CORS - allow requests from the portfolio (set ALLOWED_ORIGIN env var in production)
# Defaults to * so local dev works without any config.
_allowed_origin = os.environ.get("ALLOWED_ORIGIN", "*")
CORS(app, resources={r"/api/*": {"origins": _allowed_origin}})

# Rate limiting - prevent Gemini API abuse from public traffic
# Override with RATE_LIMIT env var if needed (e.g. "10 per minute")
_rate_limit = os.environ.get("RATE_LIMIT", "20 per minute")
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[_rate_limit],
    storage_uri="memory://",
)

# -- Pipeline (initialized once, reused across requests) --

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
    """Validate required environment variables at startup."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(
            "ERROR: GEMINI_API_KEY environment variable is not set.\n"
            "  Add it to your .env file or export it in your shell.\n"
            "  Example: export GEMINI_API_KEY=your_key_here",
            file=sys.stderr,
        )
        sys.exit(1)


# -- Routes --

@app.route("/")
def index():
    """Serve the main chat page."""
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
@limiter.limit("10 per minute")
def chat():
    """Handle a chat message and return a RAG-generated response."""
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

        return jsonify({
            "response": result["response"],
            "sources": result["sources"],
        })

    except ValueError as e:
        app.logger.error("Configuration error: %s", str(e))
        return jsonify({"error": "Server configuration error. Check the API key."}), 500
    except Exception as e:
        app.logger.error("Error processing chat request: %s", str(e))
        return jsonify({"error": "An unexpected error occurred. Please try again."}), 500


@app.route("/api/suggest", methods=["POST"])
def suggest():
    """Return suggested starter questions for the chat UI."""
    questions = [
        "Where did you grow up?",
        "What are you studying at UIUC?",
        "Tell me about the NeuroDrone project",
        "What do you work on at OPEXUS?",
        "What ML research have you done?",
        "What are your technical skills?",
    ]
    return jsonify({"questions": questions})


# -- Health check --

@app.route("/health")
def health():
    """Simple health check endpoint."""
    return jsonify({"status": "ok", "service": "ask-devansh"})


# -- Error handlers --

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


# -- Entry point --

if __name__ == "__main__":
    _check_env()

    # Eagerly initialize the pipeline so any startup errors surface immediately
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
