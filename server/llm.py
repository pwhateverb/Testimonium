import requests
import json

from openai import OpenAI


def generate_tests(requirements):
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    test_schema = {
        "requirements": {
            "type": "array",
            "description": "The requirements for which to generate test cases.",
            "items": {
                "requirement_id": {
                    "type": "string",
                    "description": "The unique ID of the requirement.",
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
    }

    completion = client.chat.completions.create(
        model="loaded_model",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant helping a software engineer generate test cases based on given requirements. The requirements are as follows:\n\n"
                + requirements
                + "\n\nPlease generate test cases for the requirements. YOU MUST ANSWER IN THE FOLLOWING JSON FORMAT:\n\n"
                + json.dumps(test_schema, indent=4)
                + "\n\nMake sure there's ONLY ONE JSON OBJECT in the response.",
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

    return completion.choices[0].message.content
