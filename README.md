# Stable Cascade in stable-diffusion-webui-Forge

## Requirements

- VRAM: 16GB?

## Screenshots

![](images/ss1.webp)

## API Endpoint

http://127.0.0.1:7860/cascade

{
"prompt" : "tshirt saying 'hello'",
"negative_prompt": "bad quality",
"width": 1024,
"height": 1024,
"guidance_scale": 4.0,
"prior_steps": 20,
"decoder_steps": 10,
"seed": -1,
"batch_size": 1
}
