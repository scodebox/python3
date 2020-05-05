import base64

opfile = open('DecodedImageFile.png','wb')
opfile.write(base64.b64decode(open('encodedImageFile','rb').read()))