from services.stego_service import (
    StegoService
)


def test_unicode_secret():

    service = StegoService()

    input_img = "tests/assets/test.png"

    output_img = "temp/unicode_test.png"

    secret = "Hello 🔐 नमस्ते こんにちは"

    service.embed(
        algorithm="lsb",
        crypto="aes",
        key="unicode123",
        cover_path=input_img,
        secret=secret,
        output_path=output_img
    )

    result = service.extract(
        algorithm="lsb",
        key="unicode123",
        stego_path=output_img
    )

    assert result == secret