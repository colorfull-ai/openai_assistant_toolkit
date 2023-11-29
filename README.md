# README for openai_assistants_toolkit

## openai_assistants_toolkit

`openai_assistants_toolkit` is a Python library designed to simplify the process of creating OpenAI assistant tools. It provides a streamlined way to generate function tools from OpenAPI JSON specifications, enabling rapid development and integration of API endpoints as tools for AI assistants.

### Features

- **Automatic Tool Generation**: Convert OpenAPI specifications into functional tools that can be used by OpenAI assistants.
- **Easy Integration**: Seamlessly integrates with OpenAI's assistant API, allowing for the quick deployment of new tools.
- **Customizable Tool Definitions**: Generate function tools with custom names, descriptions, and parameters based on your API's endpoints.

### Installation

To install `openai_assistants_toolkit`, simply run:

```bash
pip install openai_assistants_toolkit
```

### Usage

#### Basic Usage

To use `openai_assistants_toolkit`, first import the necessary classes:

```python
from openai_assistants_toolkit import FunctionToolGenerator, OpenAPISpecParser
```

Then, load your OpenAPI JSON specification and generate the tools:

```python
spec_file_path = 'path/to/your/openapi_spec.json'
with open(spec_file_path, 'r') as file:
    spec_data = json.load(file)

parser = OpenAPISpecParser(spec_data)
parsed_data = parser.parse()

generator = FunctionToolGenerator(parsed_data)
tools = generator.generate_functions()

# Now, 'tools' contains the function tools based on your API spec
```

#### Advanced Usage

For more advanced usage, refer to the documentation and examples provided in the `/examples` directory.

### Contributing

Contributions to `openai_assistants_toolkit` are welcome! Please read our [Contribution Guidelines](CONTRIBUTING.md) for more information on how to contribute.

### License

`openai_assistants_toolkit` is licensed under the [MIT License](LICENSE).

### Support

For support, please open an issue on our GitHub repository or contact us via email.

### Acknowledgments

Thanks to all contributors and users of `openai_assistants_toolkit`. Your support and feedback are invaluable to this project.

