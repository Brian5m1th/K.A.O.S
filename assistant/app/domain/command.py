from enum import Enum


class CommandType(str, Enum):
    SAVE_CONVERSATION = "save_conversation"
    SAVE_MEMORY = "save_memory"
    SEARCH_MEMORY = "search_memory"
    RECALL_MEMORY = "recall_memory"
    DELETE_MEMORY = "delete_memory"
