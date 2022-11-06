import numpy as np
from my_helpers import MyImageHelpers


def apply_new_texture(image, object_mask, texture_map):
    resulting_image = image.copy()
    masking_pixels = np.where(object_mask > 0)

    texture_pixels = masking_pixels
    x_coords = texture_pixels[0]
    y_coords = texture_pixels[1]
    x_coords = np.subtract(x_coords, min(masking_pixels[0]))
    y_coords = np.subtract(y_coords, min(masking_pixels[1]))
    texture_pixels = x_coords, y_coords, texture_pixels[2]
    w_img, h_img, c_img = image.shape
    w_text, h_text, c_text = texture_map.shape
    scale_x = (max(x_coords) - w_text + 2) / w_text
    scale_y = (max(y_coords) - h_text + 2) / h_text

    if w_img > w_text or h_img > h_text:
        texture_map = MyImageHelpers(texture_map).resize_image(1 + max(scale_x, scale_y))

    resulting_image[masking_pixels] = texture_map[texture_pixels]
    return resulting_image


