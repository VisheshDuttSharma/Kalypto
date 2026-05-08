import pytest

from services.stego_service import (
    StegoService
)


def test_capacity_limit():

    service = StegoService()

    input_img = "tests/assets/test.png"

    output_img = "temp/capacity_fail.png"

    huge_secret = "A" * 1000000

    with pytest.raises(Exception):

        service.embed(
            algorithm="lsb",
            crypto="aes",
            key="test123",
            cover_path=input_img,
            secret=huge_secret,
            output_path=output_img
        )