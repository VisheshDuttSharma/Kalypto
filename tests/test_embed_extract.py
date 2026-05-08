from services.stego_service import (
    StegoService
)


def test_embed_extract():

    service = StegoService()

    input_img = "tests/assets/test.png"

    output_img = "temp/test_output.png"

    secret = "hello world"

    service.embed(
        algorithm="lsb",
        crypto="aes",
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