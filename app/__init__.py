from flask import Flask # type: ignore

def create_app():
    app = Flask(__name__)
    
    # Import and register routes
    from app.routes import configure_routes
    configure_routes(app)
    
    return app