from pathlib import Path

from services.stego_service import (
    StegoService
)


def test_corrupted_output():

    service = StegoService()

    bad_file = "temp/corrupt.png"

    Path(bad_file).write_bytes(
        b"not a real png"
    )

    result = service.extract(
        algorithm="lsb",
        key="test123",
        stego_path=bad_file
    )

    assert result == "" or result is None