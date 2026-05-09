from services.compare_service import (
    CompareService
)


def test_report_generation():

    service = CompareService()

    report = service.build_report(
        "original.png",
        "stego.png"
    )

    assert isinstance(report, str)

    assert "KALYPTO" in report