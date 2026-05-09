import pytest

from services.stego_service import (
    StegoService
)


@pytest.mark.parametrize(
    "crypto",
    [
        "aes",
        "xor",
        "chacha20"
    ]
)
def test_multiple_crypto(
    crypto
):

    service = StegoService()

    input_img = "tests/assets/test.png"

    output_img = f"temp/{crypto}_output.png"

    secret = f"secret using {crypto}"

    service.embed(
        algorithm="lsb",
        crypto=crypto,
        key="test123",
        cover_path=input_img,
        secret=secret,
        output_path=output_img
    )

    result = service.extract(
        algorithm="lsb",
        key="test123",
        stego_path=output_img
    )

    assert result == secret
