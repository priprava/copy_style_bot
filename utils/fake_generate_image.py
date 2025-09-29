async def fake_generate_picture():
    with open("ComfyUI_00001_.png", "+rb") as png:
        return png.read()


