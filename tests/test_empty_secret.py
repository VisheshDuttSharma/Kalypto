import pytest

from services.stego_service import (
    StegoService
)


def test_empty_secret():

    service = StegoService()

    input_img = "tests/assets/test.png"

    output_img = "temp/test_empty.png"

    with pytest.raises(Exception):

        service.embed(
            algorithm="lsb",
            crypto="aes",
            key="test123",
            cover_path=input_img,
            secret="",
            output_path=output_img
        )