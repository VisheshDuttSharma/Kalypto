from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


class ExportService:

    def export_pdf(
        self,
        report_text,
        output_path
    ):

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
            12
        )

        y = 760

        for line in report_text.split("\n"):

            c.drawString(
                50,
                y,
                line[:95]
            )

            y -= 20

        c.save()