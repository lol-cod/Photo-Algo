import textwrap

# take path of image as a input
path = 'leena.png'

# taking encryption key as input
key = int(input('Enter Key for encryption of Image : '))

# print path of image file and encryption key that
# we are using
print('The path of file : ', path)
print('Key for encryption : ', key)

# open file for reading purpose
fin = open(path, 'rb')

# storing image data in variable "image"
image = fin.read()


fin.close()

# converting image into byte array to
 

image = bytearray(image)
image_len = (len(image))
n=int(input("Enter number of parts to divide the image into: "))

divided=(textwrap.wrap(image, n))
        




# performing XOR operation on each value of bytearray
for index, values in enumerate(image):
        image[index] = values ^ key

# opening file for writing purpose
fin = open(path, 'wb')

# writing encrypted data in image
fin.write(image)

fin.close()
print('Encryption Done...')


