from agent_document import DocumentAgent
from agent_excel import ExcelAgent
from agent_research import WebResearchAgent
from agent_video import VideoAgent
from agent_form import ApplicationFormAgent
from agent_qc import QualityAgent

class Jarvis:
    def __init__(self):
        self.agents = {
            "document": DocumentAgent(),
            "excel": ExcelAgent(),
            "research": WebResearchAgent(),
            "video": VideoAgent(),
            "form": ApplicationFormAgent(),
        }
        self.qc = QualityAgent()

    def plan(self, task: str):
        t = task.lower()
        plan = []
        if any(x in t for x in ["pdf", "word", "letter", "document", "दस्तावेज", "पत्र"]):
            plan.append("document")
        if any(x in t for x in ["excel", "sheet", "data", "calculation", "तालिका", "डेटा"]):
            plan.append("excel")
        if any(x in t for x in ["research", "search", "internet", "website", "जानकारी"]):
            plan.append("research")
        if any(x in t for x in ["video", "reel", "वीडियो", "रील"]):
            plan.append("video")
        if any(x in t for x in ["form", "application", "आवेदन", "फॉर्म"]):
            plan.append("form")
        return plan or ["research"]

    def run(self, task: str):
        selected = self.plan(task)
        results = [self.agents[name].run(task) for name in selected]
        return self.qc.run(task, results)
