import cv2

# считываем изображение в цвете
img = cv2.imread('images/variant-1.jpg')

# переводим изображение в полутоновое
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# сохраняем полутоновое изображение
cv2.imwrite('gray_variant-1.jpg', gray_img)

import cv2
import numpy as np

# подключаемся к камере
cap = cv2.VideoCapture(0)

# определяем цветовой диапазон для выделения метки
lower_range = np.array([0, 0, 0])    # минимальные значения BGR
upper_range = np.array([50, 50, 50]) # максимальные значения BGR

while True:
    # захватываем кадр с камеры
    _, frame = cap.read()

    # преобразуем кадр в полутоновое изображение
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # фильтруем изображение по цветовому диапазону
    mask = cv2.inRange(frame, lower_range, upper_range)

    # выделяем контуры на изображении
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # выводим координаты найденных контуров
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        print(f'Метка найдена. x={x}, y={y}')

        # выводим изображение с прямоугольной рамкой вокруг метки
        frame_with_rect = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Метка', frame_with_rect)

    # проверяем, был ли нажат ESC, чтобы выйти из цикла
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# освобождаем ресурсы и закрываем окна
cap.release()
cv2.destroyAllWindows()
