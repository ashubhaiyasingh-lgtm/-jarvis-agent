from .base import BaseAgent

class WebResearchAgent(BaseAgent):
    name = "Research Agent"
    def run(self, task):
        return f"[Research Agent] Prepared web-research workflow for: {task}"
