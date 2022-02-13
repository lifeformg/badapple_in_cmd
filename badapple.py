from PIL import Image
import time
import os
ascii_char = list("$@B%8&WM#*oaqwmZO0QLCJrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. 
#$@B%8&WM#;:,\"^`'. 

def get_char(r, b, g, alpha=256): 
	if alpha == 0: 
		return ' '
	length = len(ascii_char) 
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) 
  
	unit = (256.0 + 1)/length 
	return ascii_char[int(gray/unit)] 
	
H=50
W=188
#354 500
def printimg(path):
	tag = Image.open(path)

	tag=tag.resize((W,H),Image.NEAREST)
	ch = ""
	for i in range(H):
		for j in range(W):
			ch+=get_char(*tag.getpixel((j,i)))
		ch += '\n'

	print(ch,end='')
	
tdy=0.027
#badapple
for i in range(5355):
	a='%d'%i
	t=4-len(a)
	if(t==1):
		a='0'+a
	if(t==2):
		a='00'+a
	if(t==3):
		a='000'+a
	printimg('bad_apple_320_240_25fps\\'+a+'.jpg')
	time.sleep(tdy)


