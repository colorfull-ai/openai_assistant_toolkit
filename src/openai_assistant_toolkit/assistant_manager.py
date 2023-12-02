from openai import OpenAI


class AssistantManager:
    def __init__(self, client):
        self.client: OpenAI = client

    def list_assistants(self):
        try:
            assistants = self.client.beta.assistants.list()
            return assistants.data
        except Exception as e:
            print(f"Error listing assistants: {e}")
            return None

    def get_assistant(self, asst_id):
        try:
            assistant = self.client.beta.assistants.retrieve(asst_id)
            return assistant.data
        except Exception as e:
            print(f"Error getting assistant: {e}")
            return None

    def get_assistant_info(self, asst_id):
        try:
            assistant = self.client.beta.assistants.retrieve(asst_id)
            return assistant.json()
        except Exception as e:
            print(f"Error getting assistant: {e}")
            return None

