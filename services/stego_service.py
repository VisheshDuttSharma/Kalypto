from pathlib import Path

from PIL import (
    UnidentifiedImageError
)

from engine.pipeline import (
    StegoPipeline,
    PipelineConfig
)


class StegoService:

    def embed(
        self,
        algorithm,
        crypto,
        key,
        cover_path,
        secret,
        output_path
    ):

        if not secret:
            raise ValueError(
                "Secret message cannot be empty."
            )

        cfg = PipelineConfig(
            algorithm=algorithm,
            encrypt=True,
            crypto_algo=crypto,
            key=key
        )

        pipeline = StegoPipeline(cfg)

        pipeline.encode(
            str(Path(cover_path)),
            secret,
            str(Path(output_path))
        )

        return str(Path(output_path))

    def extract(
        self,
        algorithm,
        key,
        stego_path
    ):

        try:

            cfg = PipelineConfig(
                algorithm=algorithm,
                encrypt=True,
                key=key
            )

            pipeline = StegoPipeline(cfg)

            result = pipeline.decode(
                str(Path(stego_path))
            )

            return result

        except (
            FileNotFoundError,
            ValueError,
            UnidentifiedImageError,
            OSError
        ):

            return None