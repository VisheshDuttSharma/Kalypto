from services.stego_service import (
    StegoService
)


def test_wrong_key():

    service = StegoService()

    input_img = "tests/assets/test.png"

    output_img = "temp/test_wrong_key.png"

    secret = "hidden message"

    service.embed(
        algorithm="lsb",
        crypto="aes",
        key="correct123",
        cover_path=input_img,
        secret=secret,
        output_path=output_img
    )

    result = service.extract(
        algorithm="lsb",
        key="wrongkey",
        stego_path=output_img
    )


    assert result == "" or result is None