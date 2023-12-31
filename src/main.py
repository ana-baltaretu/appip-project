from my_configuration import *
from my_helpers import MyImageHelpers
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
        input_image = MyImageHelpers(input_image).resize_image(4)  # For "vase.jpg" needs to be larger
        print("Read input image of size:", input_image.shape)
        mask_image = cv2.imread(input_masks_path)
        mask_image = MyImageHelpers(mask_image).resize_image(4)  # For "vase.jpg" needs to be larger
        print("Read mask of size:", mask_image.shape)
        texture_image = cv2.imread(input_texture_path)
        print("Read texture of size:", texture_image.shape)
        return input_image, mask_image, texture_image
    except:
        print("Error: Make sure to add your input image in [../input/images/], "
              "input mask in [../input/masks/] and input texture in [../input/textures/]")
    return None, None, None


def apply_masking(input_image, mask_image):
    masked_object = np.zeros(input_image.shape)
    print(input_image.shape)
    masked_pixels = np.where(mask_image > 0)
    masked_object[masked_pixels] = input_image[masked_pixels]
    return masked_object


def generate_maps(masked_object):
    # Generates intensity, specularity and normals
    generate_intensity_map(masked_object)
    intensity_map = cv2.imread(output_intensity_avg, cv2.IMREAD_GRAYSCALE)

    generate_specularity_map(intensity_map)
    specularity_image = cv2.imread(output_specularity_map, cv2.IMREAD_GRAYSCALE)

    generate_normal_map(intensity_map)
    normal_image = cv2.imread(output_normal_map)
    return specularity_image, normal_image


def write_latest_run(src_img, mask, texture_image,
                     normal_map, specularity_map, applied_texture):
    # Write everything in the latest run folder
    cv2.imwrite(latest_run_source, src_img)
    cv2.imwrite(latest_run_mask, mask)
    cv2.imwrite(latest_run_texture, texture_image)
    cv2.imwrite(latest_run_normal_map, normal_map)
    cv2.imwrite(latest_run_specularity_map, specularity_map)
    cv2.imwrite(latest_run_applied_texture, applied_texture)


# TODO: RUN THIS BEFORE BLENDER SCRIPT!!!!!!!!!!!!
if __name__ == '__main__':
    generate_folder_structure()

    # Reading
    input_image, mask_image, texture_image = read_all_inputs()

    # Get only the object for which we are applying texture to
    masked_object = apply_masking(input_image, mask_image)

    # Map generation
    specularity_image, normal_image = generate_maps(masked_object)

    # Replacing object material with texture
    resulting_image = apply_new_texture(input_image, mask_image, texture_image)

    # Writing
    cv2.imwrite(output_applied_texture, resulting_image)
    write_latest_run(input_image, mask_image, texture_image,
                     normal_image, specularity_image, resulting_image)

    # Blender stuff
    # TODO: GO TO BLENDER PROJECT NOW
    # TODO: THEN GO TO "my_post_blender_script.py"
