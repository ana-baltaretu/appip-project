from my_configuration import *


def apply_textured_object(input_image, final_image, mask_image):
    result_image = input_image.copy()
    masked_pixels = np.where(mask_image > 0)
    result_image[masked_pixels] = final_image[masked_pixels]
    cv2.imwrite(result_image_path, result_image)
    return


if __name__ == '__main__':
    input_image = cv2.imread(input_images_path)
    # resulting_image = cv2.imread(output_applied_texture)
    mask_image = cv2.imread(input_masks_path)

    # Check shape and maybe fixes
    final_image = cv2.imread(final_applied_maps)
    # w1, h1, c1 = resulting_image.shape

    w2, h2, c2 = final_image.shape
    apply_textured_object(input_image, final_image, mask_image)