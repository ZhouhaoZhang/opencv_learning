import cv2


def show(image,name="res"):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def bgr2rgb(image_bgr):
    b, g, r = cv2.split(image_bgr)
    img_rgb = cv2.merge((r, g, b))
    return img_rgb


if __name__ == "__main__":
    img = cv2.imread('test.jpg')
    show('hahaha', img)
