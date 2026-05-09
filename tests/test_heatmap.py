from pathlib import Path

from services.compare_service import (
    CompareService
)


def test_heatmap_generation():

    service = CompareService()

    original = "tests/assets/test.png"

    stego = "tests/assets/test.png"

    result = service.generate_heatmap(
        original,
        stego
    )

    assert Path(result).exists()