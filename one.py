import cv2
image = cv2.imread("C:\pythonProjectmuha/image.jpg")
# Загружаем предобученную модель для лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Преобразуем в ч/б
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Находим лица
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Рисуем прямоугольники вокруг лиц
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow("Найденные лица", image)
cv2.waitKey(0)
cv2.destroyAllWindows() 