import pytest

from services.stego_service import (
    StegoService
)


def test_invalid_input_file():

    service = StegoService()

    invalid_file = "tests/assets/fake.txt"

    output_img = "temp/fake_output.png"

    with pytest.raises(Exception):

        service.embed(
            algorithm="lsb",
            crypto="aes",
            key="test123",
            cover_path=invalid_file,
            secret="hello",
            output_path=output_img
        )