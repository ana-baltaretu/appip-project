from my_configuration import *


def generate_intensity_map(source_image):
    intensity_map = np.sum(source_image, axis=2) / 3  # AVG on the color channels
    cv2.imwrite(output_intensity_avg, intensity_map)
    return intensity_map


def generate_specularity_map(source_image, contrast=1.6, brightness=0.55):
    intensity_map = generate_intensity_map(source_image)
    intensity_map *= brightness
    too_bright_pixels = np.where(intensity_map > 255.0)
    intensity_map[too_bright_pixels] = 255.0
    specularity_map = ((((intensity_map/255.0)-0.5)*contrast)+0.5)*255.0
    cv2.imwrite(input_specularity_map, specularity_map)
    return specularity_map


def apply_sobel():
    return


def generate_normal_map():
    return

