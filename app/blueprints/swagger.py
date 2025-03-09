from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
# API_URL = 'static/swagger/swagger.yaml'  # Our API url (can of course be a local resource)
API_URL = '/static/swagger/swagger.yaml'  # Use absolute path starting with '/'
# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
)
