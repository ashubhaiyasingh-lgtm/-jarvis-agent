from .base import BaseAgent

class ApplicationFormAgent(BaseAgent):
    name = "Application Form Agent"
    def run(self, task):
        return (
            f"[Application Form Agent] Prepared form workflow for: {task}\n"
            "It can prepare/fill fields and attachments. Final Submit must require explicit user confirmation."
        )
