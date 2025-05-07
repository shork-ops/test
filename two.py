from skimage import io
import matplotlib.pyplot as plt
from skimage.transform import resize, rescale

# Новый URL изображения (с прямым доступом)
url = "https://img3.procvetok.com/crop/w500h500/32/a0/32a074858cfe875cb16d47a91e7d3c93.jpg"
image = io.imread(url)
# Масштабирование (изменение размера в 50% от оригинала)
scaled_image = rescale(image, 0.5, anti_aliasing=True)


# Создаём 2 подграфика для отображения оригинального и изменённого изображений
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(scaled_image)
ax[0].set_title("Scaled (50%)")
ax[0].axis("off")
plt.show()