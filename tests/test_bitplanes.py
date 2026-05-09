from pathlib import Path

from services.compare_service import (
    CompareService
)


def test_bitplane_generation():

    service = CompareService()

    result = service.generate_bitplane(
        "tests/assets/test.png",
        0
    )

    assert Path(result).exists()