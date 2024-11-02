import numpy
import cv2


def main():
    real_image = cv2.imread("photo_with_ball.jpg")
    gray_image = cv2.imread("photo_with_ball.jpg", 0)
    cv2.imshow("result", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
