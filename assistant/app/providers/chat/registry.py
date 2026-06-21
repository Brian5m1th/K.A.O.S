from app.providers.chat.ollama import OllamaChatProvider
from app.providers.chat.openai import OpenAIChatProvider
from app.providers.chat.anthropic import AnthropicChatProvider
from app.providers.chat.gemini import GeminiChatProvider
from app.providers.base.chat import BaseChatProvider
from app.registry.service_registry import ServiceRegistry


def register_chat_providers() -> None:
    ServiceRegistry.register_chat_provider("ollama", OllamaChatProvider)
    ServiceRegistry.register_chat_provider("openai", OpenAIChatProvider)
    ServiceRegistry.register_chat_provider("anthropic", AnthropicChatProvider)
    ServiceRegistry.register_chat_provider("gemini", GeminiChatProvider)
