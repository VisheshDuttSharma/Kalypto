import pytest

from services.stego_service import (
    StegoService
)


def test_corrupted_image():

    service = StegoService()

    corrupted = "tests/assets/corrupted.png"

    output_img = "temp/corrupted_output.png"

    with pytest.raises(Exception):

        service.embed(
            algorithm="lsb",
            crypto="aes",
            key="test123",
            cover_path=corrupted,
            secret="hello",
            output_path=output_img
        )