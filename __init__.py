from .prompt_studio_node import WAN22PromptStudioNode

NODE_CLASS_MAPPINGS = {
    "WAN22PromptStudioNode": WAN22PromptStudioNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WAN22PromptStudioNode": "WAN 2.2 Prompt Studio"
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]