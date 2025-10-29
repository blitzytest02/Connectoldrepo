"""
Pytest Configuration and Fixtures
==================================

This module provides pytest configuration and reusable test fixtures
for the Flask application test suite.
"""

import pytest
from app import create_app


@pytest.fixture
def app():
    """
    Create and configure a Flask application instance for testing.

    This fixture provides a Flask application configured for testing,
    with test-specific settings that override production configurations.

    Yields:
        Flask application instance configured for testing
    """
    # Create app with test configuration
    test_config = {
        "TESTING": True,
        "SECRET_KEY": "test-secret-key",
        "ENVIRONMENT": "testing",
    }

    app = create_app(config=test_config)

    # Set up application context
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    """
    Create a test client for the Flask application.

    This fixture provides a test client that can be used to make
    requests to the application without running a server.

    Args:
        app: Flask application fixture

    Returns:
        Flask test client
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """
    Create a CLI runner for testing Flask CLI commands.

    Args:
        app: Flask application fixture

    Returns:
        Flask CLI test runner
    """
    return app.test_cli_runner()
