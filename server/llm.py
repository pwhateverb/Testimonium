import requests
import json

from openai import OpenAI


def generate_tests(requirements):
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    test_schema = {
        "requirements": [
            {
                "requirement_id": "The unique ID of the requirement.",
                "test_cases": [
                    {
                        "description": "The description of the test case.",
                        "expected_result": "The expected result of the test case.",
                    }
                ],
            }
        ]
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
                + "\n\nMake sure there's ONLY ONE JSON OBJECT in the response and NOTHING else. The fields 'requirements' and 'test_cases' are lists containing instances of the respective objects. The 'requirement_id' field is a unique ID for the requirement, and the 'description' and 'expected_result' fields are strings describing the test case and the expected result, respectively.",
            }
        ],
    )

    return completion.choices[0].message.content
