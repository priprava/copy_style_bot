async def fake_generate_picture(style: str):
    strength = style["config"]["strength_model"]
    clip = style["config"]["strength_clip"]
    file = style["file"]
    with open("ComfyUI_00001_.png", "+rb") as png:
        return png.read()


