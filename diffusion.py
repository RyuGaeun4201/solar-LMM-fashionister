'''
This script provides example api calls for AUTOMATIC1111/stable-diffusion-webui
Check port in `webui-user.sh` and specify it with `--port` flag. (Default: 7860)

1. Run server
2. Unzip the 'pose.tar'. Set the 'pose_dir_path' and 'result_dir_path' variables. (#revised)
3. $ python person_patch_generator_example.py --port 7860
4. Check result image in 'result_dir_path'
'''
import requests
from PIL import Image
import io
import base64
from argparse import ArgumentParser

import os
import random
import math
import datetime
import time
import pytz

parser = ArgumentParser()
parser.add_argument('--port', type=int, default=7860)
parser.add_argument('--txt2img', action='store_true')
args = parser.parse_args()


url = f'http://127.0.0.1:{args.port}/'
url_txt2img = url + 'sdapi/v1/txt2img'

BATCH_SIZE = 2

# Model specific options
model_options = {
    'base': {
        'sd_model_checkpoint': 'v1-5-pruned-emaonly.safetensors [6ce0161689]',
        # 'sd_vae': 'vae-ft-mse-840000-ema-pruned.ckpt',
        'steps': 20,
        # variables
        # 'restore_faces': True,
        # 'tiling': False,
        # 'batch_count': 1,
        # "batch_size": BATCH_SIZE,
        # 'cfg_scale': 15,
        "width" : 512,
        "height" : 768
    }
}

model_name = 'base'
model_option = model_options[model_name]

def pil_to_base64(pil_image):
    with io.BytesIO() as stream:
        pil_image.save(stream, "PNG", pnginfo=None)
        base64_str = str(base64.b64encode(stream.getvalue()), "utf-8")
        return "data:image/png;base64," + base64_str

KST = pytz.timezone('Asia/Seoul')
now = datetime.datetime.now(KST)
result_dir_path = "outputs" # revised

payload = {
            "width" : model_option["width"],
            "height" : model_option["height"],
            # 'restore_faces': model_option['restore_faces'],
            "steps": model_option['steps'],
            # "batch_count": model_option['batch_count'],
            # "batch_size": model_option['batch_size'],
            # 'cfg_scale': model_option['cfg_scale'],
            'do_not_save_samples': True,
            'do_not_save_grid': True,
            ############## Quality related options
            # 'tiling': model_option['tiling'],
            ############## Hire Fix related options
            # "enable_hr": True,
            'denoising_strength': 0.3, # 0 = same to orig, 1 = totally different from orig, default=0.75
            # "hr_scale": 1,
            # "hr_upscaler": "4x-UltraSharp",
            # "hr_second_pass_steps": 30,
}

if not os.path.exists(result_dir_path) :
    os.mkdir(result_dir_path)

def diffusion(pos_prompt) :

    result_path0 = f"{result_dir_path}/result.jpg"
    
    default_prompt = "8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3, photorealistic, highly detailed, head-to-toe shot, full-length portrait, full-body, balanced, "
    negative_prompt = "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, body out of frame, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, low contrast, high contrast, The body is naked, The outfit is topless or insufficiently-dressed, revealing clothes, torn clothes"

    model_option["prompt"] = default_prompt + pos_prompt
    model_option["negative_prompt"] = negative_prompt

    # Run t2i or i2i
    payload["prompt"] = model_option["prompt"]
    payload["negative_prompt"] = model_option["negative_prompt"]

    start_time = time.time()

    response = requests.post(url=url_txt2img, json=payload)

    response.raise_for_status()

    r = response.json()
    new_img0 = Image.open(io.BytesIO(base64.b64decode(r['images'][0].split(',', 1)[0])))
    new_img0.save(result_path0)

    end_time = time.time()
    print(str(round(end_time - start_time, 3)))

diffusion("30 years old girl wearing yellow shirt and blue jean")