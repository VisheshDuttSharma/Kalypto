from pathlib import Path


def test_pathlib_compatibility():

    path = Path("temp") / "cross_platform.txt"

    path.write_text("hello")

    assert path.exists()

    assert path.read_text() == "hello"

    path.unlink()
