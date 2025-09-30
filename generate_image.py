import random, os
from comfy_api_simplified import ComfyApiWrapper, ComfyWorkflowWrapper
import nest_asyncio
from config import STYLE, COMFY_API
nest_asyncio.apply()

api = ComfyApiWrapper(f"http://{COMFY_API}")

print(f"http://{COMFY_API}")

wf = ComfyWorkflowWrapper(os.path.abspath("workflow.json"))

async def generate_picture(style: str, prompt: str):
    print(style)
    strength = STYLE[style]["model_strenght"]
    clip = STYLE[style]["model_clip"]
    file = STYLE[style]["file"]
    positive = STYLE[style]["positive"]
    negative = STYLE[style]["negative"]

    wf.set_node_param(
        title="KSampler",
        param="seed",
        value=random.randint(0, 2**63 - 1)
    )

    positive_def = wf.get_node_param(title="positive", param="text")
    negative_def = wf.get_node_param(title="negative", param="text")


    wf.set_node_param(title="Стиль", param="lora_name", value=file)
    wf.set_node_param(title="Стиль", param="strength_model", value=strength)
    wf.set_node_param(title="Стиль", param="strength_clip", value=clip)
    wf.set_node_param(title="positive", param="text", value=f""" {positive_def}, {positive}, 
                       {prompt} """)
    

    wf.set_node_param(title="negative", param="text", value=f"{negative_def}, {negative}")
 
    results = api.queue_and_wait_images(wf, "Save Image")

    for _, image_data in results.items():
        return image_data






