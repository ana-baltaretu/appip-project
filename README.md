# Applied Image Processing Project

Group 28: Material Editing and Extraction  
Project: BSDF shader with Normal and Specularity Maps  
Author: Ana Băltăreţu  

## Setup
1. Install opencv `pip3 install opencv-python`
2. Install Blender and get the blender python extension  

Small (side) note: for me at least even after installing the `bpy` library it still doesn't recognize it in Pycharm, so if you want to edit the code just do it directly in the editor from Blender.

## Running
1. Add the input files you need (image, mask, texture) in their respective input folders, for example:
   1. [Input image with Vase at `input/images/vase.jpg`](input/images/vase.jpg)
   2. [Input image mask at `input/masks/my_vase.png`](input/masks/my_vase.png)
   3. [Input texture at `input/textures/waves.jpg`](input/textures/waves.jpg)
2. Go to [`src/main.py`](src/main.py) and run it.
3. Open the Blender project from [`src/blender_project.blend`](src/blender_project.blend)
   1. (Optional) If the input image has a different size (pixels) than the vase.jpg image, DELETE the cube element from collection.
   2. Go to the `Scripting` tab and run the code.
   3. Click `Render` > `Render Image` > `Image` > `Save as`, and save the image in [`output/latest_run` as `7_blender_output.jpg`](output/latest_run/7_blender_output.jpg)
4. Go back to the Python project to [`src/my_post_blender_script.py`](src/my_post_blender_script.py) and run it.
5. Your result should now appear at [`output/latest_run/8_results.jpg`](output/latest_run/8_results.jpg)

## Relevant methods
Note: everything from `src` is my code, written from scratch.

1. Most important [generate_normal_map and generate_specularity_map from `src/my_map_generators.py`](src/my_map_generators.py), but tbh the entire file is pretty nice.
2. I guess also the [blender script from `src/my_blender_scripts.py`](src/my_blender_scripts.py) are cool. Who knew you can code in Blender? I for sure didn't until now :O.