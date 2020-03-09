from PIL import Image, ImageChops

img1 = Image.open("C://Users//Areej//Desktop//ML project//img1.jpg")
img2 = Image.open("C://Users//Areej//Desktop//ML project//img2.jpg")

diff = ImageChops.difference(img1,img2)

if diff.getbbox():
    diff.show()