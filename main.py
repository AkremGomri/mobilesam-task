from fastapi import FastAPI, File, UploadFile
import os
from PIL import Image
import io
from fastapi.responses import Response, StreamingResponse
import subprocess

# from predict import segment_everything

app = FastAPI()

@app.post("/segment-image/")
async def segment_image(file: UploadFile):

    # Reading the image and saving it in `resources` folder
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    image_path = "resources/uploaded_image.jpg"
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    image.save(image_path)

    # Processing the image and then saving it to `generated` folder
    output_path = "generated/output.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    subprocess.run(["venv\\Scripts\\activate", "&&", "python", "segment_image.py", image_path, output_path], shell=True)

    with open(output_path, "rb") as f:
        image_bytes = f.read()

    return Response(content=image_bytes, media_type="image/png")
