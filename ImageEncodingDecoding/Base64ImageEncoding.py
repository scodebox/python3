import base64


with open('image.png','rb') as img:
	encodedImage = base64.b64encode(img.read())

with open('encodedImageFile','wb') as f:
	f.write(encodedImage)
	f.close()