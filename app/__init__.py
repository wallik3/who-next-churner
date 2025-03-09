from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp, url_prefix='/user')

    # Setup Swagger UI
    SWAGGER_URL = '/swagger'  # URL for accessing Swagger UI
    API_URL = '/static/swagger/swagger.json'  # Swagger JSON file location

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "My Flask API"}
    )

    # Register the Swagger UI blueprint
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app