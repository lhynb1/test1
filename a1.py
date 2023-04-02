from PIL import Image
im=Image.open("C:\\Users\\李鹤阳\\Desktop\\210402103339-8-1200.jpg")
im.show()
im.rotate(45)
im.show()
out=im.transpose(Image.FLIP_LEFT_RIGHT)
out.show