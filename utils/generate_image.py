import random
from comfy_api_simplified import ComfyApiWrapper, ComfyWorkflowWrapper
import nest_asyncio
from config import STYLE
nest_asyncio.apply()

api = ComfyApiWrapper()
wf = ComfyWorkflowWrapper("workflow.json")

async def generate_picture(style: str, prompt: str):
    strength = STYLE[style]["config"]["strength_model"]
    clip = STYLE[style]["config"]["strength_clip"]
    file = STYLE[style]["file"]

    wf.set_node_param(
        title="KSampler",
        param="seed",
        value=random.randint(0, 2**63 - 1)
    )

    wf.set_node_param(title="LoraLoader", param="lora_name", value=file)
    wf.set_node_param(title="LoraLoader", param="strength_model", value=strength)
    wf.set_node_param(title="LoraLoader", param="strength_clip", value=clip)
    wf.set_node_param(title="positive", param="text", value=f"""masterpiece, best quality, highly detailed,different scenery, vivid colors, immersive background 
                       {prompt} 
                       <lora:{style}:0.6>""")
 
    results = api.queue_and_wait_images(wf, "Save Image")

    for _, image_data in results.items():
        return image_data






