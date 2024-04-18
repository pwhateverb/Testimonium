import requests
import json

from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

requirements = """Functional requirements
The user shall be able to view and manage plants
The system shall notify the user when the conditions for a plant (moisture, temperature, humidity or light) are not perfect
The system shall show the user the current conditions for a plant (level of light, temperature, humidity and moisture)
The system shall provide statistics on how the moisture, humidity, temperature and light change over time
The system shall provide onboarding to show how to use the app
The system shall provide a list of plant species for the user to choose from
The system shall provide specific details about each species in the species list
The user shall be able to view and manage their rooms"""

test_schema = {
    "type": "object",
    "properties": {
        "requirement_id": {
            "type": "string",
            "description": "The ID of the requirement.",
        },
        "test_cases": {
            "type": "array",
            "description": "The test cases for the requirement.",
            "items": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "The description of the test case.",
                    },
                    "expected_result": {
                        "type": "string",
                        "description": "The expected result of the test case.",
                    },
                },
            },
        },
    },
}

completion = client.chat.completions.create(
    model="loaded_model",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant helping a software engineer generate test cases based on given requirements. The requirements are as follows:\n\n" + requirements + "\n\nPlease generate test cases for the requirements. THE TEST CASES SHOULD BE IN THE FOLLOWING FORMAT:\n\n" + json.dumps(test_schema, indent=4) + "\n\n",
        }
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "generate_tests",
                "description": "Generate test cases based on given requirements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "requirements": {
                            "type": "array",
                            "description": "The requirements for which to generate test cases.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "details": {
                                        "type": "string",
                                        "description": "The description of the requirement.",
                                    },
                                    "id": {
                                        "type": "string",
                                        "description": "Generated ID for the requirement.",
                                    },
                                },
                            },
                        },
                    },
                    "required": ["requirements"],
                },
            },
        }
    ],
)

print(completion.choices[0].message)
