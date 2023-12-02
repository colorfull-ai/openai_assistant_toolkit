from openai import OpenAI

class ConversationManager:
    def __init__(self, client, assistant_id, thread_id=None,):
        self.client: OpenAI = client
        self.assistant_id = assistant_id
        self.current_thread_id = thread_id
        self.current_run = None

    def create_conversation(self):
        if not self.current_thread_id:
            self.current_thread_id = self.client.beta.threads.create()
        return self.current_thread_id

    def add_message(self, message: str):
        if not self.current_thread_id:
            raise Exception("No active conversation thread.")
        return self.client.beta.threads.messages.create(
            thread_id=self.current_thread_id.id,
            content=message,
            role="user"
        )

    def process_conversation(self):
        if not self.current_thread_id:
            raise Exception("No active conversation thread.")
        self.current_run = self.client.beta.threads.runs.create(
            thread_id=self.current_thread_id.id,
            assistant_id=self.assistant_id
        )

        while self.current_run.status not in ["cancelled", "cancelling", "completed", "failed", "expired"]:
            self.current_run = self.client.beta.threads.runs.retrieve(
                thread_id=self.current_thread_id.id,
                run_id=self.current_run.id
            )
        messages = self.client.beta.threads.messages.list(
            thread_id=self.current_thread_id.id
        )
        return messages