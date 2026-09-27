from openpyxl import Workbook
from datetime import datetime
from pathlib import Path


class ExcelAgent:
    name = "ExcelAgent"

    def run(self, task):
        output = Path("jarvis_output.xlsx")

        wb = Workbook()

        # Monthly Data sheet
        ws = wb.active
        ws.title = "Monthly Data"

        headers = [
            "Date",
            "Item / Activity",
            "Quantity",
            "Unit",
            "Amount",
            "Remarks"
        ]

        ws.append(headers)
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = "A1:F1"

        # Summary sheet
        summary = wb.create_sheet("Summary")

        summary["A1"] = "JARVIS Excel Report"
        summary["A2"] = "Task"
        summary["B2"] = task
        summary["A3"] = "Created"
        summary["B3"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        summary["A5"] = "Status"
        summary["B5"] = "Excel file successfully generated"

        # Column widths
        widths = {
            "A": 15,
            "B": 30,
            "C": 15,
            "D": 15,
            "E": 15,
            "F": 35
        }

        for column, width in widths.items():
            ws.column_dimensions[column].width = width

        summary.column_dimensions["A"].width = 20
        summary.column_dimensions["B"].width = 60

        wb.save(output)

        return (
            f"[ExcelAgent] Excel file created: {output.name}\n"
            f"Task: {task}\n"
            "Excel report successfully generated."
        )
