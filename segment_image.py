import os
import sys
import numpy as np
import torch
from mobile_sam import SamAutomaticMaskGenerator, SamPredictor, sam_model_registry
from PIL import Image

from tools import box_prompt, format_results, point_prompt, fast_process

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

sam_checkpoint = "./mobile_sam.pt"
model_type = "vit_t"

mobile_sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
mobile_sam = mobile_sam.to(device=device)
mobile_sam.eval()

mask_generator = SamAutomaticMaskGenerator(mobile_sam)
predictor = SamPredictor(mobile_sam)

@torch.no_grad()
def segment_everything(
    image,
    input_size=1024,
    better_quality=False,
    withContours=True,
    use_retina=True,
    mask_random_color=True,
):
    global mask_generator

    input_size = int(input_size)
    w, h = image.size
    scale = input_size / max(w, h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    image = image.resize((new_w, new_h))

    nd_image = np.array(image)
    annotations = mask_generator.generate(nd_image)

    fig = fast_process(
        annotations=annotations,
        image=image,
        device=device,
        scale=(1024 // input_size),
        better_quality=better_quality,
        mask_random_color=mask_random_color,
        bbox=None,
        use_retina=use_retina,
        withContours=withContours,
    )
    return fig

def process_image(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    image = Image.open(input_path).convert("RGB")
    fig = segment_everything(
        image=image
    )
    fig.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py input_image_path output_image_path")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    process_image(input_path, output_path)
