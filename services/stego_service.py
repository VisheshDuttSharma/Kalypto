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

        if not secret.strip():
            raise ValueError(
                "Secret message cannot be empty."
            )
        cfg = PipelineConfig(
            algorithm=algorithm,
            encrypt=bool(key),
            crypto_algo=crypto,
            key=key or "defaultkey"
        )

        StegoPipeline(cfg).encode(
            cover_path,
            secret,
            output_path
        )

        return output_path


    def extract(
        self,
        algorithm,
        key,
        stego_path
    ):

        cfg = PipelineConfig(
            algorithm=algorithm,
            encrypt=bool(key),
            key=key or "defaultkey"
        )

        result = StegoPipeline(cfg).decode(
            stego_path
        )

        return result