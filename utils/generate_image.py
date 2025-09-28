import random
from comfy_api_simplified import ComfyApiWrapper, ComfyWorkflowWrapper

api = ComfyApiWrapper()
wf = ComfyWorkflowWrapper("/content/copy_style_bot/utils/workflow.json")

async def generate_picture(style: str, prompt: str):
    wf.set_node_param(
        title="KSampler",
        param="seed",
        value=random.randint(0, 2**63 - 1)
    )

    wf.set_node_param(title="positive", param="text", value=f"<lora:{style}:1> " + prompt)
 
    results = api.queue_and_wait_images(wf, "Save Image")

    for _, image_data in results.items():
        return image_data


