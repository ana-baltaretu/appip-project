import cv2
from my_helpers import MyImageHelpers
from my_configuration import *
from my_map_generators import *
from my_texture_application import *


if __name__ == '__main__':
    input_image = cv2.imread(input_images_path)
    MyImageHelpers(input_image).show_smaller_image()


# //setup generator and calculate map
# NormalmapGenerator normalmapGenerator(mode, redMultiplier, greenMultiplier, blueMultiplier, alphaMultiplier);
# normalmap = normalmapGenerator.calculateNormalmap(inputScaled, kernel, strength, invert, tileable, keepLargeDetail, largeDetailScale, largeDetailHeight);
# normalmapRawIntensity = normalmapGenerator.getIntensityMap().convertToQImage();