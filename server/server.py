from flask import Flask
import json
import llm
import sys

from flask import request

from flask_cors import CORS

app = Flask(__name__)

# Define CORS options
cors_config = {
    "origins": ["http://localhost:8080", "http://localhost:3000"],
    "supports_credentials": True,
    "methods": ["GET", "HEAD", "PUT", "PATCH", "POST", "DELETE"],
    "allowed_headers": ["X-Secret", "X-API-Version", "Content-Type", "Authorization"],
}

# Enable CORS for your Flask app
CORS(app, **cors_config)


@app.get("/")
def get_tests():
    json_response = string_to_json(llm.generate_tests(request.args.get("requirements")))
    print(json_response, file=sys.stdout)
    return json_response


def string_to_json(string):
    start = string.find("{")
    end = string.rfind("}")
    string = string[start : end + 1]
    return json.loads(string)
