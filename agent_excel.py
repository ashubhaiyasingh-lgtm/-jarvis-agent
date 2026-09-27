from .base import BaseAgent

class ExcelAgent(BaseAgent):
    name = "Excel Agent"
    def run(self, task):
        return f"[Excel Agent] Prepared data/Excel workflow for: {task}"
