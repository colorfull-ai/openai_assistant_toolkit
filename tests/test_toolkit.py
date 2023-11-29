# test_toolkit.py
from openai_assistant_toolkit import FunctionToolGenerator  # Replace 'your_module' with the actual module name
from openai_assistant_toolkit import OpenAPISpecParser  # Replace 'your_module' with the actual module name

def test_generate_functions_with_valid_data():
    parsed_data = {
        "endpoints": [
            {
                "name": "TestEndpoint",
                "description": "Test Description",
                "parameters": {
                    "type": "object",
                    "properties": {"param1": {"type": "string"}},
                    "required": ["param1"]
                }
            }
        ]
    }
    generator = FunctionToolGenerator(parsed_data)
    functions = generator.generate_functions()

    assert len(functions) == 1
    assert functions[0]["type"] == "function"
    assert functions[0]["function"]["name"] == "TestEndpoint"
    assert functions[0]["function"]["description"] == "Test Description"
    assert "param1" in functions[0]["function"]["parameters"]["properties"]


def test_parse_valid_spec():
    spec_data = {
        "openapi": "3.1.0",
        "paths": {
            "/test": {
                "get": {
                    "operationId": "TestOperation",
                    "description": "Test operation",
                    "parameters": [
                        {
                            "name": "param1",
                            "in": "query",
                            "required": True,
                            "schema": {"type": "string"},
                            "description": "A test parameter"
                        }
                    ]
                }
            }
        }
    }
    parser = OpenAPISpecParser(spec_data)
    parsed_data = parser.parse()

    assert len(parsed_data["endpoints"]) == 1
    endpoint = parsed_data["endpoints"][0]
    assert endpoint["name"] == "TestOperation"
    assert endpoint["description"] == "Test operation"
    assert endpoint["parameters"]["properties"]["param1"]["type"] == "string"
    assert "param1" in endpoint["parameters"]["required"]
