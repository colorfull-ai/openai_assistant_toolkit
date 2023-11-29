import json

class FunctionToolGenerator:
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data

    def generate_functions(self):
        # Use parsed data to generate function definitions
        # Each function corresponds to an API endpoint
        functions = []
        for endpoint in self.parsed_data['endpoints']:
            function = self._create_function_tool(endpoint)
            functions.append(function)
        return functions

    def _create_function_tool(self, endpoint):
        # Generate a single function tool configuration
        # This is a helper method used by generate_functions
        return {
            "type": "function",
            "function": {
                "name": endpoint['name'],
                "description": endpoint['description'],
                "parameters": endpoint['parameters']
            }
        }


class OpenAPISpecParser:
    def __init__(self, spec_data):
        self.spec_data = spec_data

    def parse(self):
        endpoints = []
        for path, operations in self.spec_data["paths"].items():
            for method, details in operations.items():
                endpoint = self._parse_endpoint(path, method, details)
                endpoints.append(endpoint)
        return {"endpoints": endpoints}

    def _parse_endpoint(self, path, method, details):
        # Convert the OpenAPI parameters to the format expected by the tool
        parameters = self._convert_parameters(details.get("parameters", []))

        return {
            "name": details.get("operationId", ""),
            "description": details.get("description", ""),
            "method": method,
            "path": path,
            "parameters": parameters
        }

    def _convert_parameters(self, parameters):
        # Converts OpenAPI parameters to the required format
        tool_parameters = {
            "type": "object",
            "properties": {},
            "required": []
        }

        for param in parameters:
            param_name = param.get("name")
            tool_parameters["properties"][param_name] = {
                "type": param.get("schema", {}).get("type", "string"),
                "description": param.get("description", "")
            }
            if param.get("required", False):
                tool_parameters["required"].append(param_name)

        return tool_parameters

def create_toolkit_from_openapi_spec(spec_file_path):
    with open(spec_file_path, 'r') as file:
        spec_data = json.load(file)

    parser = OpenAPISpecParser(spec_data)
    parsed_data = parser.parse()

    generator = FunctionToolGenerator(parsed_data)
    function_tools = generator.generate_functions()

    return function_tools