class BaseAgent:
    name = "base"
    def run(self, task: str):
        raise NotImplementedError
