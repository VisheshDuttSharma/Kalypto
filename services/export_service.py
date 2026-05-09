from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


class ExportService:

    def export_pdf(
        self,
        report_text,
        output_path
    ):

        output_path = str(
            Path(output_path)
        )

        c = canvas.Canvas(
            output_path,
            pagesize=A4
        )

        c.setFont(
            "Helvetica-Bold",
            18
        )

        c.drawString(
            50,
            800,
            "Kalypto Report"
        )

        c.setFont(
            "Helvetica",
            11
        )

        y = 760

        for line in report_text.splitlines():

            c.drawString(
                50,
                y,
                line[:110]
            )

            y -= 18

            if y < 50:

                c.showPage()

                c.setFont(
                    "Helvetica",
                    11
                )

                y = 800

        c.save()

        return output_path