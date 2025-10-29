"""
Application Tests
=================

This module contains tests for the Flask application's core functionality,
including route validation, configuration, and basic API behavior.
"""

import json
from app import create_app


class TestApplicationFactory:
    """Tests for the application factory function."""

    def test_create_app_returns_flask_instance(self):
        """Test that create_app returns a Flask application instance."""
        app = create_app()
        assert app is not None
        assert app.name == "app"

    def test_create_app_with_custom_config(self):
        """Test that create_app accepts and applies custom configuration."""
        custom_config = {"TESTING": True, "CUSTOM_VALUE": "test123"}
        app = create_app(config=custom_config)
        assert app.config["TESTING"] is True
        assert app.config["CUSTOM_VALUE"] == "test123"

    def test_create_app_has_secret_key(self):
        """Test that the application has a secret key configured."""
        app = create_app()
        assert "SECRET_KEY" in app.config
        assert app.config["SECRET_KEY"] is not None


class TestRootEndpoint:
    """Tests for the root endpoint (/)."""

    def test_root_endpoint_exists(self, client):
        """Test that the root endpoint is accessible."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_endpoint_returns_json(self, client):
        """Test that the root endpoint returns JSON response."""
        response = client.get("/")
        assert response.content_type == "application/json"

    def test_root_endpoint_response_structure(self, client):
        """Test that the root endpoint returns expected data structure."""
        response = client.get("/")
        data = json.loads(response.data)

        assert "status" in data
        assert "message" in data
        assert "environment" in data
        assert data["status"] == "success"

    def test_root_endpoint_message(self, client):
        """Test that the root endpoint returns correct message."""
        response = client.get("/")
        data = json.loads(response.data)
        assert data["message"] == "Flask application is running"


class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_endpoint_exists(self, client):
        """Test that the health endpoint is accessible."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_endpoint_returns_json(self, client):
        """Test that the health endpoint returns JSON response."""
        response = client.get("/health")
        assert response.content_type == "application/json"

    def test_health_endpoint_response_structure(self, client):
        """Test that the health endpoint returns expected data structure."""
        response = client.get("/health")
        data = json.loads(response.data)

        assert "status" in data
        assert "service" in data
        assert data["status"] == "healthy"
        assert data["service"] == "flask-migration-poc"


class TestAPIStatusEndpoint:
    """Tests for the API status endpoint."""

    def test_api_status_endpoint_exists(self, client):
        """Test that the API status endpoint is accessible."""
        response = client.get("/api/status")
        assert response.status_code == 200

    def test_api_status_returns_json(self, client):
        """Test that the API status endpoint returns JSON response."""
        response = client.get("/api/status")
        assert response.content_type == "application/json"

    def test_api_status_response_structure(self, client):
        """Test API status endpoint returns expected data structure."""
        response = client.get("/api/status")
        data = json.loads(response.data)

        assert "api" in data
        assert "version" in data
        assert "framework" in data
        assert "python_version" in data

    def test_api_status_values(self, client):
        """Test that the API status endpoint returns correct values."""
        response = client.get("/api/status")
        data = json.loads(response.data)

        assert data["api"] == "active"
        assert data["version"] == "1.0.0"
        assert "Flask" in data["framework"]


class TestErrorHandling:
    """Tests for error handling and edge cases."""

    def test_404_for_nonexistent_route(self, client):
        """Test that accessing a non-existent route returns 404."""
        response = client.get("/nonexistent-route")
        assert response.status_code == 404

    def test_405_for_wrong_method(self, client):
        """Test that using wrong HTTP method returns 405."""
        # Root endpoint only accepts GET, not POST
        response = client.post("/")
        assert response.status_code == 405


class TestApplicationConfiguration:
    """Tests for application configuration."""

    def test_testing_config_is_active(self, app):
        """Test that testing configuration is properly applied."""
        assert app.config["TESTING"] is True

    def test_environment_is_set(self, app):
        """Test that environment is properly configured."""
        assert "ENVIRONMENT" in app.config
        assert app.config["ENVIRONMENT"] == "testing"
