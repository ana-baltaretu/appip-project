import os
import cv2
import numpy as np
from scipy.ndimage.filters import convolve


folder_names = ["../input/", "../output/", "../input/images/", "../input/textures/",
                "../input/masks/", "../output/normal_maps/", "../output/specularity_maps/",
                "../output/intensities/", "../output/applied_textures/", "../output/latest_run"]

image_name = "nefertitti.png"
texture_name = "ana.jpg"
mask_name = "nefertitti_hat_no_background.png"
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
latest_run_normal_map = "../output/latest_run/2_normal_map.jpg"
latest_run_specularity_map = "../output/latest_run/3_specularity_map.jpg"
latest_run_applied_texture = "../output/latest_run/4_applied_texture.jpg"

final_applied_maps = "../output/final/nefertiti_waves_with_specularity-rendered_final.jpg"
result_image_path = "../output/results/" + image_name[:(len(image_name) - 3)] + "_" + texture_name

