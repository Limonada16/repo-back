from PIL import Image
from PIL import ImageEnhance

img = Image.open("gato.jpg")
#Imagen con brillo en 1
applier = ImageEnhance.Brightness(img)
img2 = applier.enhance(1)
#Iamgen con contraste en 6
applier2 = ImageEnhance.Contrast(img2)
img3 = applier2.enhance(2)



img3.show()

