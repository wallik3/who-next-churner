from flask import Flask, request, jsonify, render_template
import pandas as pd
import traceback
import os

from src.model import inference, MODEL_FEATURE
import app.blueprints as blueprint

# Initiate App  
app = Flask(__name__, template_folder = './app/templates', static_folder = './app/static')

app.register_blueprint(blueprint.inference_blueprint, url_prefix="/inference")
app.register_blueprint(blueprint.swaggerui_blueprint, url_prefix="/swagger")

@app.route("/health")
def health():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)