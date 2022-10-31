import cv2


class MyImageHelpers:
    img = None
    resized_image = None

    def __init__(self, img):
        self.img = img
        self.resized_image = None
        return

    def show_image(self):
        cv2.imshow('image', self.img)
        cv2.waitKey(0)

    def show_resized_image(self):
        if self.resized_image is not None:
            cv2.imshow('image', self.resized_image)
            cv2.waitKey(0)
        else:
            print("image wasn't resized yet!")

    def resize_image(self, times):
        """
        Resizes an image 'times' larger or smaller, uses interpolation to not mess it up
        :param img: the image you want to resize
        :param times: how big you want it to be
        positive numbers = that many times larger (+2 => 2 times larger)
        negative numbers = that many times larger (-5 => 5 times smaller)
        :return:
        """
        if times < 0:
            times = 1 / (-times)
        width = int(self.img.shape[1] * times)
        height = int(self.img.shape[0] * times)
        self.resized_image = cv2.resize(self.img, (width, height), interpolation=cv2.INTER_AREA)
        return self.resized_image

    def show_smaller_image(self):
        self.resize_image(-5)
        self.show_resized_image()


