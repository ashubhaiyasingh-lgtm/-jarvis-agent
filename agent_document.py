from .base import BaseAgent

class DocumentAgent(BaseAgent):
    name = "Document Agent"
    def run(self, task):
        return f"[Document Agent] Prepared document workflow for: {task}"
