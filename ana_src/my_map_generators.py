from my_configuration import *
from my_helpers import MyImageHelpers


def generate_intensity_map(source_image):
    intensity_map = np.max(source_image, axis=2)  # AVG on the color channels
    cv2.imwrite(output_intensity_avg, intensity_map)
    return


def generate_specularity_map(intensity_map, contrast=1.6, brightness=0.55):
    intensity_map = intensity_map.astype(np.float64)
    intensity_map *= brightness

    # Capping upper to 255
    too_bright_pixels = np.where(intensity_map > 255.0)
    intensity_map[too_bright_pixels] = 255.0

    # Specularity map generation
    specularity_map = ((intensity_map - 127.5) * contrast + 127.5)

    # Capping lower to 0
    too_dark_pixels = np.where(specularity_map < 0.0)
    specularity_map[too_dark_pixels] = 0.0

    # Write
    cv2.imwrite(output_specularity_map, specularity_map)
    return


def apply_sobel(intensity_map):
    intensity_map = (255 - intensity_map).astype(np.float64)
    w, h = intensity_map.shape
    filtered_map = np.zeros((w, h, 3), np.float64)

    # Sobel filters for convolution to calculate the gradient (normal)
    sobel_x = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]], np.float64)
    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]], np.float64)

    output_x = convolve(intensity_map.copy(), sobel_x)
    output_x[np.where(output_x < -255.0)] = -255.0
    output_x[np.where(output_x > 255.0)] = 255.0
    # output_x = output_x / np.max(output_x) * 255.0
    output_y = convolve(intensity_map.copy(), sobel_y)
    output_y[np.where(output_y < -255.0)] = -255.0
    output_y[np.where(output_y > 255.0)] = 255.0
    # output_y = output_y / np.max(output_y) * 255.0

    # Default color for normal maps is this purple pixel: BGR(255, 127.5, 127.5)
    # Put calculated gradients in the correct color channels (and fill blue channel)
    filtered_map[:, :, 0] = np.full((w, h), 255.0)  # B
    filtered_map[:, :, 1] = output_y  # G
    filtered_map[:, :, 2] = output_x  # R

    return filtered_map


# Similar algorithm to "soft light" from Photoshop,
# see https://photoshoptrainingchannel.com/blending-modes-explained/
def blend_soft_light(src_1, src_2):
    image1 = src_1.copy().astype(np.uint8)
    image2 = src_2.copy().astype(np.uint8)
    result = np.zeros(image1.shape)

    pixels_case_1 = np.where(2.0 * image2 < 255.0)
    pixels_case_2 = np.where(2.0 * image2 >= 255.0)

    result[pixels_case_1] = ((image1[pixels_case_1] + 127.5) * image2[pixels_case_1]) / 255.0
    result[pixels_case_2] = 255.0 - ((382.5 - image1[pixels_case_2]) * (255.0 - image2[pixels_case_2]) / 255.0)

    return result.astype(np.uint8)


# large_detail_scale
def generate_normal_map(intensity_map, keep_large_detail=True, large_detail_scale=-3):
    filtered_map = apply_sobel(intensity_map)

    # Converting from [-255,255] to [0,255]
    normal_map = ((filtered_map + 255.0) / 2.0).astype(np.uint8)

    # If we want to keep the general geometry in mind we would want to keep the large details
    if keep_large_detail is True:
        # Make a downscaled image
        downscaled_intensity_map = MyImageHelpers(intensity_map).resize_image(large_detail_scale)

        # Make small
        downscaled_normal_map = generate_normal_map(downscaled_intensity_map, keep_large_detail=False)

        # Make back to big but without nice interpolation (so it's a bit chunky)
        rescaled_normal_map = MyImageHelpers(downscaled_normal_map).resize_image(-large_detail_scale, interpolation=cv2.INTER_CUBIC)

        # Blend downscaled image with the normal one
        normal_map = blend_soft_light(normal_map, rescaled_normal_map)

    # Write
    cv2.imwrite(output_normal_map, normal_map)
    return normal_map



