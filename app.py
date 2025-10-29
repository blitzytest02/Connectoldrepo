"""
Minimal Flask Application - Proof of Concept
==============================================

This is a minimal Flask application created to validate the development
environment setup. It serves as a proof-of-concept demonstrating that:
- Flask is properly installed and configured
- The application can start and respond to requests
- The testing infrastructure is functional

This file should be replaced with the full Flask application once the
Node.js source code is available for migration.
"""

from flask import Flask, jsonify
from flask_cors import CORS
import os


def create_app(config=None):
    """
    Application factory function.

    Creates and configures the Flask application instance.
    This follows Flask best practices for testability and flexibility.

    Args:
        config: Optional configuration dictionary

    Returns:
        Flask application instance
    """
    app = Flask(__name__)

    # Load configuration
    secret_default = "dev-secret-key-change-in-production"
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", secret_default)
    app.config["ENVIRONMENT"] = os.getenv("FLASK_ENV", "development")

    # Apply custom configuration if provided
    if config:
        app.config.update(config)

    # Enable CORS
    CORS(app)

    # Register routes
    @app.route("/")
    def index():
        """
        Root endpoint - Health check.

        Returns:
            JSON response with status and message
        """
        return jsonify(
            {
                "status": "success",
                "message": "Flask application is running",
                "environment": app.config["ENVIRONMENT"],
            }
        )

    @app.route("/health")
    def health():
        """
        Health check endpoint.

        Returns:
            JSON response indicating service health
        """
        return jsonify({"status": "healthy", "service": "flask-migration-poc"})

    @app.route("/api/status")
    def api_status():
        """
        API status endpoint.

        Returns:
            JSON response with API information
        """
        return jsonify(
            {
                "api": "active",
                "version": "1.0.0",
                "framework": "Flask 3.0.0",
                "python_version": "3.12.3",
            }
        )

    return app


# Create application instance for direct execution
app = create_app()


if __name__ == "__main__":
    """
    Development server entry point.

    This runs the Flask development server when app.py is executed directly.
    For production, use: gunicorn app:app
    """
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV") == "development"

    print(f"Starting Flask application on port {port}...")
    print(f"Environment: {os.getenv('FLASK_ENV', 'development')}")
    print(f"Debug mode: {debug}")

    app.run(host="0.0.0.0", port=port, debug=debug)
