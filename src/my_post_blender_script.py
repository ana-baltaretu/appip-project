from my_configuration import *
from my_helpers import MyImageHelpers


def apply_textured_object(src, blender, mask):
    masked_pixels = np.where(mask == 0)
    blender[masked_pixels] = src[masked_pixels]
    cv2.imwrite(latest_run_results, blender)
    return


if __name__ == '__main__':
    input_image = cv2.imread(latest_run_applied_texture)
    mask_image = cv2.imread(latest_run_mask)
    final_image = cv2.imread(latest_run_blender_output)

    apply_textured_object(input_image, final_image, mask_image)