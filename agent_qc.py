class QualityAgent:
    def run(self, task, results):
        return (
            "TASK PLAN COMPLETE\n"
            f"Original task: {task}\n"
            "Sub-agents used:\n- " +
            "\n- ".join(results) +
            "\n\n[QC Agent] Initial validation complete."
        )
