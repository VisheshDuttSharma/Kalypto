import uuid

from services.stego_service import (
    StegoService
)


def test_algorithms():

    service = StegoService()

    algorithms = [
        "lsb",
        "adaptive_lsb",
        "pvd"
    ]

    for algo in algorithms:

        input_img = "tests/assets/test.png"

        output_img = (
            f"temp/{algo}_{uuid.uuid4().hex}.png"
        )

        secret = f"secret for {algo}"

        service.embed(
            algorithm=algo,
            crypto="aes",
            key="algo123",
            cover_path=input_img,
            secret=secret,
            output_path=output_img
        )

        result = service.extract(
            algorithm=algo,
            key="algo123",
            stego_path=output_img
        )

        assert result == secret