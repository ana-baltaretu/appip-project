import os
import cv2
import numpy as np
from scipy.ndimage.filters import convolve


folder_names = ["../input/", "../output/", "../input/images/", "../input/textures/",
                "../input/masks/", "../output/normal_maps/", "../output/specularity_maps/",
                "../output/intensities/", "../output/applied_textures/", "../output/latest_run"]

# nefertitti.png, vase.jpg
image_name = "nefertitti.png"
    # bubbly_0083, bubbly_0159, honeycombed_0053, honeycombed_0117, pebbles, other_pebbles, veined_0094, veined_0179
texture_name = "honeycombed_0053.jpg"
mask_name = "nefertitti_hat_no_background.png"  # "nefertitti_hat_no_background.png
normal_map_name = "nefertitti_hat_no_background_normal.png"
specularity_map_name = "nefertitti_hat_no_background_spec.png"

input_images_path = "../input/images/" + image_name
input_texture_path = "../input/textures/" + texture_name
input_masks_path = "../input/masks/" + mask_name
input_normal_map = "../output/normal_maps/" + normal_map_name
output_specularity_map = "../output/specularity_maps/" + specularity_map_name

output_intensity_avg = "../output/intensities/avg_" + image_name
output_intensity_spec = "../output/intensities/spec_" + image_name
output_normal_map = "../output/normal_maps/" + image_name
output_applied_texture = "../output/applied_textures/" + image_name[:(len(image_name) - 3)] + "_" + texture_name

latest_run_source = "../output/latest_run/1_source.jpg"
latest_run_mask = "../output/latest_run/2_mask.png"
latest_run_texture = "../output/latest_run/3_texture.png"
latest_run_normal_map = "../output/latest_run/4_normal_map.jpg"
latest_run_specularity_map = "../output/latest_run/5_specularity_map.png"
latest_run_applied_texture = "../output/latest_run/6_applied_texture.jpg"
latest_run_blender_output = "../output/latest_run/7_blender_output.jpg"
latest_run_results = "../output/latest_run/8_results.jpg"

final_applied_name = "vase_waves.jpg"  # "nefertiti_waves_with_specularity-rendered_final.jpg"
final_applied_maps = "../output/final/" + final_applied_name
result_image_path = "../output/results/" + image_name[:(len(image_name) - 3)] + "_" + texture_name

