import launch

try:
  from diffusers import StableCascadeDecoderPipeline
except:
  launch.run_pip(f"install --upgrade diffusers")
