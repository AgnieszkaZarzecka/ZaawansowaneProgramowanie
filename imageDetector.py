import time
from os import listdir
import cv2
import imutils

def detect_human(file_name):
    start = time.time()
    hogcv = cv2.HOGDescriptor()
    hogcv.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    image = cv2.imread('Images/' + file_name)

    image = imutils.resize(image,
                           width=min(500, image.shape[1]))

    (humans, _) = hogcv.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(16, 16),
                                            scale=1.07
                                            )

    for (x, y, w, h) in humans:
        cv2.rectangle(image, (x, y),
                      (x + w, y + h),
                      (0, 255, 0), 3)

    print('W pliku %s znaleziono %i ludzi w czasie %s s' % (file_name, len(humans), str(time.time() - start)))
    cv2.imshow('IMG', image)
    cv2.waitKey(0)

def detector():
    file_list = listdir('./Images')
    print(file_list)
    file_name = input('Podaj nazwę pliku(--all jeśli wszystkie) \n')
    if file_name == '--all':
        for file in file_list:
            detect_human(file)
    else:
        if file_name in file_list:
            detect_human(file_name)
        else:
            print('Taki plik nie istnieje')