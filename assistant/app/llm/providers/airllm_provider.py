import asyncio
from typing import AsyncIterator, Iterator

from langchain_core.messages import BaseMessage, AIMessage
from loguru import logger

from app.llm.provider import BaseProvider


class AirLLMProvider(BaseProvider):
    def __init__(self, model: str, **kwargs):
        self._model = model
        self._kwargs = kwargs
        self._model_instance = None
        logger.info(f"AirLLMProvider initialized for model: {self._model}")

    def _get_model(self):
        """Lazy-load AirLLM AutoModel to save memory during startup."""
        if self._model_instance is None:
            logger.info(f"[airllm] Lazy-loading model layers for: {self._model}")
            try:
                from airllm import AutoModel
                # AutoModel automatically detects and splits models (llama, qwen, etc.)
                self._model_instance = AutoModel(self._model, **self._kwargs)
            except Exception as e:
                logger.error(f"[airllm] Failed to load AirLLM AutoModel: {e}")
                raise RuntimeError(f"Failed to load AirLLM: {e}") from e
        return self._model_instance

    def _messages_to_prompt(self, messages: list[BaseMessage]) -> str:
        """Translate LangChain messages list to a formatted text prompt."""
        prompt = ""
        for msg in messages:
            if msg.type == "system":
                prompt += f"System: {msg.content}\n"
            elif msg.type == "human":
                prompt += f"User: {msg.content}\n"
            elif msg.type == "ai":
                prompt += f"Assistant: {msg.content}\n"
        prompt += "Assistant: "
        return prompt

    def _sync_generate(self, prompt: str) -> str:
        """Run blocking model generation synchronously."""
        model = self._get_model()
        input_ids = model.tokenizer(prompt, return_tensors="pt").input_ids
        # Perform layer-wise inference
        output_ids = model.generate(input_ids, max_new_tokens=128)
        output_text = model.tokenizer.decode(output_ids[0])
        # Strip the input prompt from the output if returned
        if output_text.startswith(prompt):
            output_text = output_text[len(prompt):]
        return output_text.strip()

    def invoke(self, messages: list[BaseMessage]) -> BaseMessage:
        prompt = self._messages_to_prompt(messages)
        output = self._sync_generate(prompt)
        return AIMessage(content=output)

    async def ainvoke(self, messages: list[BaseMessage]) -> BaseMessage:
        # Run the blocking GPU/CPU generation in a separate thread pool
        prompt = self._messages_to_prompt(messages)
        output = await asyncio.to_thread(self._sync_generate, prompt)
        return AIMessage(content=output)

    def stream(self, messages: list[BaseMessage]) -> Iterator[BaseMessage]:
        # AirLLM processes layer-by-layer and does not support native real-time token streaming.
        # Fall back to single-step completion.
        yield self.invoke(messages)

    async def astream(self, messages: list[BaseMessage]) -> AsyncIterator[BaseMessage]:
        # AirLLM processes layer-by-layer and does not support native real-time token streaming.
        # Fall back to single-step completion.
        yield await self.ainvoke(messages)

    @property
    def model_name(self) -> str:
        return self._model

    @property
    def provider_name(self) -> str:
        return "airllm"
