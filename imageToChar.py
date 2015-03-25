import cv2
import sys

#adjust the odering of the characters in the below list for getting better art. This is hit and trial process
ASCII_CHARS = ['!','"','#','$','%','&','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']

def getCharData(img, widthInChar=128):

	#resize the image so as to get the width as 128(default) characters
	(height,width) = img.shape
	comRatio = height/(widthInChar*1.0)
	newHeight = widthInChar
	newWidth = int(width/comRatio)

	img = cv2.resize(img, (newHeight,newWidth))

	asciiLen = len(ASCII_CHARS)

	data = ""

	# traverse through each pixel of image
	for row in img:
		for x in row:
			data += ASCII_CHARS[x/30]	# change 30 to as per ur wish
		data += "\n"

	return data


if __name__ == "__main__":
	
	try:
		imageName = sys.argv[1]
	except:
		print "\nUsage: python "+sys.argv[0]+" imageFile.jpg [outputfile.txt]\n"
		sys.exit()


	try:
		# read image in graysacle mode so as to get a 2-D vector having values between 0-255
		img = cv2.imread(imageName,cv2.IMREAD_GRAYSCALE)
		data = getCharData(img)
		print data

	except:
		
		print "\nInvalid image file \n"
		sys.exit()

	# write data to a text file
	if len(sys.argv) == 3:
		outFile = sys.argv[2]
		f = open(outFile,'w')
		f.write(data)
		f.close()