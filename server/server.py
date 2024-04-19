from flask import Flask
import json
import llm

from flask import request

app = Flask(__name__)

@app.get('/')
def get_tests():
    return string_to_json(llm.generate_tests(request.args.get('requirements')))

def string_to_json(string):
    start = string.find('{')
    end = string.rfind('}')
    string = string[start:end+1]
    return json.loads(string)