	#Dcrypting image 
	
try:

	path = input(r'Enter path of Image : ')                       # take path of image as a input
	
	
	key = int(input('Enter Key for encryption of Image : '))      # taking decryption key as input
	
	print('The path of file : ', path)                            # print path of image file and decryption key that we are using
	print('Note : Encryption key and Decryption key must be same.')
	print('Key for Decryption : ', key)
	
	
	fin = open(path, 'rb')                                         # open file for reading purpose
	
	image = fin.read()                                            # storing image data in variable "image"
	                                                            
	fin.close()
	
	
	image = bytearray(image)                                      # converting image into byte array to perform decryption easily on numeric data

	# performing XOR operation on each value of bytearray
	for index, values in enumerate(image):
		image[index] = values ^ key

	fin = open(path, 'wb')                                        # opening file for writing purpose
	
	
	fin.write(image)                                              # writing decryption data in image
	fin.close()
	print('Decryption Done...')


except Exception:
	print('Error caught : ', Exception.__name__)


