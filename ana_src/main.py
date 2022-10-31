import os.path

import cv2
from my_helpers import MyImageHelpers
from my_configuration import *
from my_map_generators import *
from my_texture_application import *


def generate_folder_structure():
    for folder in folder_names:
        if not os.path.isdir(folder):
            os.mkdir(folder)
    return


def read_all_inputs():
    try:
        input_image = cv2.imread(input_images_path)
        print("Read input image of size:", input_image.shape)
        mask_image = cv2.imread(input_masks_path)
        print("Read mask of size:", mask_image.shape)
        texture_image = cv2.imread(input_texture_path)
        print("Read texture of size:", texture_image.shape)
        normal_image = cv2.imread(input_normal_map)
        specularity_image = cv2.imread(input_specularity_map)
        return input_image, mask_image, texture_image, normal_image, specularity_image
    except:
        print("Error: Make sure to add your input image in [../input/images/], "
              "input mask in [../input/masks/] and input texture in [../input/textures/]")
    return None, None, None, None, None

def write_latest_run(src_img, normal_map, specularity_map, applied_texture):
    cv2.imwrite(latest_run_source, src_img)
    cv2.imwrite(latest_run_normal_map, normal_map)
    cv2.imwrite(latest_run_specularity_map, specularity_map)
    cv2.imwrite(latest_run_applied_texture, applied_texture)


if __name__ == '__main__':
    generate_folder_structure()

    # Reading
    input_image, mask_image, texture_image, normal_image, specularity_image = read_all_inputs()
    MyImageHelpers(input_image).show_smaller_image()

    resulting_image = apply_new_texture(input_image, mask_image, texture_image)

    cv2.imwrite(output_applied_texture, resulting_image)
    write_latest_run(input_image, normal_image, specularity_image, resulting_image)

    MyImageHelpers(resulting_image).show_smaller_image()
