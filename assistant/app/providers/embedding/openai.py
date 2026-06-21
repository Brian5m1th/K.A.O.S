from loguru import logger

from app.providers.base.embedding import BaseEmbeddingProvider


class OpenAIEmbeddingProvider(BaseEmbeddingProvider):
    provider_name = "openai"

    def __init__(self, api_key: str = "", model: str = "text-embedding-3-small", base_url: str = ""):
        self._api_key = api_key
        self._model = model
        self._base_url = base_url or "https://api.openai.com/v1"

    async def embed(self, text: str) -> list[float]:
        logger.info("[start] OpenAIEmbeddingProvider - embed")
        result = (await self.embed_batch([text]))[0]
        logger.debug("[finish] OpenAIEmbeddingProvider - embed")
        return result

    async def embed_batch(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"[start] OpenAIEmbeddingProvider - embed_batch size={len(texts)}")

        import httpx
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "input": texts,
            "model": self._model,
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self._base_url}/embeddings",
                json=payload,
                headers=headers,
            )
            response.raise_for_status()
            data = response.json()

        data_by_index = sorted(data["data"], key=lambda x: x["index"])
        logger.debug("[finish] OpenAIEmbeddingProvider - embed_batch")
        return [item["embedding"] for item in data_by_index]

    async def healthcheck(self) -> bool:
        try:
            await self.embed("healthcheck")
            return True
        except Exception:
            return False
