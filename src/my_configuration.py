import os
import cv2
import numpy as np
from scipy.ndimage.filters import convolve


folder_names = ["../input/", "../output/", "../input/images/", "../input/textures/",
                "../input/masks/", "../output/normal_maps/", "../output/specularity_maps/",
                "../output/intensities/", "../output/applied_textures/", "../output/latest_run"]

########################################################
### vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
### TODO: CHANGE VARIABLES TO WHATEVER U NEED BELOW HERE

# nefertitti.png, vase.jpg
image_name = "vase.jpg"  # TODO: Put other images in "../input/images/" folder

# waves, bubbly_0083, bubbly_0159, honeycombed_0053, honeycombed_0117, pebbles1, pebbles2, veined_0094, veined_0179
texture_name = "veined_0179.jpg"  # TODO: Put other masks in "../input/masks/" folder

# "nefertitti_hat_no_background.png, my_vase.png
mask_name = "my_vase.png"  # TODO: Put other textures in "../input/textures/" folder

### TODO: CHANGE VARIABLES TO WHATEVER U NEED ABOVE HERE
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
########################################################

input_images_path = "../input/images/" + image_name
input_texture_path = "../input/textures/" + texture_name
input_masks_path = "../input/masks/" + mask_name

output_intensity_avg = "../output/intensities/avg_" + image_name
output_specularity_map = "../output/specularity_maps/" + image_name
output_normal_map = "../output/normal_maps/" + image_name
output_applied_texture = "../output/applied_textures/" + image_name[:(len(image_name) - 4)] + "_" + texture_name

latest_run_source = "../output/latest_run/1_source.jpg"
latest_run_mask = "../output/latest_run/2_mask.png"
latest_run_texture = "../output/latest_run/3_texture.png"
latest_run_normal_map = "../output/latest_run/4_normal_map.jpg"
latest_run_specularity_map = "../output/latest_run/5_specularity_map.png"
latest_run_applied_texture = "../output/latest_run/6_applied_texture.jpg"
latest_run_blender_output = "../output/latest_run/7_blender_output.jpg"
latest_run_results = "../output/latest_run/8_results.jpg"

result_image_path = "../output/results/" + image_name[:(len(image_name) - 3)] + "_" + texture_name

