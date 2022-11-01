from my_configuration import *


def generate_intensity_map(source_image):
    intensity_map = np.sum(source_image, axis=2) / 3  # AVG on the color channels
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
    output_x = output_x / np.max(np.abs(output_x)) * 255.0
    output_y = convolve(intensity_map.copy(), sobel_y)
    output_y = output_y / np.max(np.abs(output_y)) * 255.0

    # Default color for normal maps is this purple pixel: BGR(255, 127.5, 127.5)
    # Put calculated gradients in the correct color channels (and fill blue channel)
    filtered_map[:, :, 0] = np.full((w, h), 255.0)  # B
    filtered_map[:, :, 1] = output_y  # G
    filtered_map[:, :, 2] = output_x  # R

    return filtered_map


def generate_normal_map(intensity_map):
    filtered_map = apply_sobel(intensity_map)

    # Converting from [-255,255] to [0,255]
    normal_map = ((filtered_map + 255.0) / 2.0).astype(np.uint64)

    # Write
    cv2.imwrite(output_normal_map, normal_map)
    return

