import cv2
import time
from grabscreen import grab_screen
from lifx import get_lifx_bulb
import os
# import numpy as np
# import colorsys
# from sklearn.cluster import KMeans
# from collections import Counter


# credits: https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
def convert_to_hsv(dom):
    # R, G, B values are divided by 255
    # to change the range from 0..255 to 0..1:
    b, g, r, _ = dom
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # h, s, v = hue, saturation, value
    cmax = max(r, g, b)    # maximum of r, g, b
    cmin = min(r, g, b)    # minimum of r, g, b
    diff = cmax-cmin       # diff of cmax and cmin.

    # if cmax and cmax are equal then h = 0
    if cmax == cmin:
        h = 0

    # if cmax equal r then compute h
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360

    # if cmax equal g then compute h
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360

    # if cmax equal b then compute h
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    # if cmax equal zero
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100

    # compute v
    v = cmax * 100
    return [int(h*65535/360), int(s*65535/100), int(v*65535/100), 3500]


def process_img(image):
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)

    return processed_img


if __name__ == "__main__":
    for i in list(range(3))[::-1]:
        print(i+1)
        time.sleep(.1)

    bulb = get_lifx_bulb()

    last_time = time.time()

    blank_image = cv2.imread("blank.png")

    dev = True

    while True:
        screen = grab_screen(region=(0, 0, 1920, 1080))
        # print('Frame took {} seconds'.format(time.time()-last_time)) # Seconds per frame
        # print('{} FPS'.format(1/(time.time()-last_time))) #Frames per second
        last_time = time.time()
        resized = cv2.resize(screen, (480, 270), interpolation=cv2.INTER_AREA)
        new_screen = process_img(resized)

        dom_color = cv2.mean(new_screen)
        color_hsv = convert_to_hsv(dom_color)
        bulb.set_color(color_hsv, 150, rapid=False)
        b, g, r, _ = [int(x) for x in dom_color]
        cv2.rectangle(blank_image,
                      (0, 0),
                      (480, 270),
                      color=(b, g, r), thickness=-1)
        if dev == True:
            print(dom_color, color_hsv)
            cv2.imshow('window1', new_screen)
            cv2.imshow('window2', blank_image)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# credits: https://adamspannbauer.github.io/2018/03/02/app-icon-dominant-colors/
# def get_dominant_color(image, k=4, image_processing_size=None):
#     """
#     takes an image as input
#     returns the dominant color of the image as a list

#     dominant color is found by running k means on the
#     pixels & returning the centroid of the largest cluster

#     processing time is sped up by working with a smaller image;
#     this resizing can be done with the image_processing_size param
#     which takes a tuple of image dims as input

#     >>> get_dominant_color(my_image, k=4, image_processing_size = (25, 25))
#     [56.2423442, 34.0834233, 70.1234123]
#     """
#     # resize image if new dims provided
#     if image_processing_size is not None:
#         image = cv2.resize(image, image_processing_size,
#                            interpolation=cv2.INTER_AREA)

#     # reshape the image to be a list of pixels
#     image = image.reshape((image.shape[0] * image.shape[1], 3))

#     # cluster and assign labels to the pixels
#     clt = KMeans(n_clusters=k)
#     labels = clt.fit_predict(image)

#     # count labels to find most popular
#     label_counts = Counter(labels)

#     # subset out most popular centroid
#     dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
#     return list(dominant_color)


# def crop(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
#     # Now find contours in it. There will be only one object, so find bounding rectangle for it.

#     contours, hierarchy = cv2.findContours(
#         thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnt = contours[0]
#     x, y, w, h = cv2.boundingRect(cnt)
#     # Now crop the image, and save it into another file.
#     crop = image[y:y+h, x:x+w]
#     return crop
