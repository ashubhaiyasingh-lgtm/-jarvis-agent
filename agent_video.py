from .base import BaseAgent

class VideoAgent(BaseAgent):
    name = "Video Agent"
    def run(self, task):
        return (
            f"[Video Agent] Prepared video workflow for: {task}\n"
            "Next integration: video generation/editing provider."
        )
