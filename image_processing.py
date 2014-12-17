from PIL import Image, ImageFilter
import sys

PIXEL_BLOCKS = 10

try:
	original = Image.open("test2.bmp")
except Exception as e:
	print(str(e))

print("The size of the image is:")
print(original.format, original.size, original.mode)
#exit()
im_width, im_height = original.size

if(original.mode == "L"):
	for y in range(0, int(im_height / PIXEL_BLOCKS)):
		for x in range(0, int(im_width / PIXEL_BLOCKS)):
			r = 0
			#print()
			for p in range(PIXEL_BLOCKS):
				xy = (x * PIXEL_BLOCKS + p, y * PIXEL_BLOCKS + p)
				#print(xy)
				r += original.getpixel(xy)
			r = r/PIXEL_BLOCKS
			
			if(r < 16):
				sys.stdout.write("  ")
			elif(r > 15 and r < 32):
				sys.stdout.write("* ")
			elif(r > 31 and r < 48):
				sys.stdout.write(",,")
			elif(r > 47 and r < 64):
				sys.stdout.write("^^")
			elif(r > 63 and r < 80):
				sys.stdout.write("||")
			elif(r > 79 and r < 96):
				sys.stdout.write("0^")
			elif(r > 95 and r < 112):
				sys.stdout.write("P_")
			elif(r > 111 and r < 128):
				sys.stdout.write(".(")
			elif(r > 127 and r < 144):
				sys.stdout.write("SS")
			elif(r > 143 and r < 160):
				sys.stdout.write("//")
			elif(r > 159 and r < 174):
				sys.stdout.write("CC")
			elif(r > 173 and r < 190):
				sys.stdout.write("??")
			elif(r > 189 and r < 206):
				sys.stdout.write("RR")
			elif(r > 205 and r < 222):
				sys.stdout.write("##")
			elif(r > 221 and r < 238):
				sys.stdout.write("$$")
			elif(r > 237 and r < 255):
				sys.stdout.write("QQ")
			else:
				sys.stdout.write("  ")
		print()			

if(original.mode == "RGB"):
	for y in range(0, int(im_height / PIXEL_BLOCKS)):
		for x in range(0, int(im_width / PIXEL_BLOCKS)):
			r = 0
			#print()
			for p in range(PIXEL_BLOCKS):
				xy = (x * PIXEL_BLOCKS + p, y * PIXEL_BLOCKS + p)
				#print(xy)
				red, green, blue = original.getpixel(xy)
				r += (red + green + blue) / 3
			r = r/PIXEL_BLOCKS

			if(r < 16):
				sys.stdout.write("  ")
			elif(r > 15 and r < 32):
				sys.stdout.write("* ")
			elif(r > 31 and r < 48):
				sys.stdout.write(",,")
			elif(r > 47 and r < 64):
				sys.stdout.write("^^")
			elif(r > 63 and r < 80):
				sys.stdout.write("||")
			elif(r > 79 and r < 96):
				sys.stdout.write("0^")
			elif(r > 95 and r < 112):
				sys.stdout.write("P_")
			elif(r > 111 and r < 128):
				sys.stdout.write(".(")
			elif(r > 127 and r < 144):
				sys.stdout.write("SS")
			elif(r > 143 and r < 160):
				sys.stdout.write("//")
			elif(r > 159 and r < 174):
				sys.stdout.write("CC")
			elif(r > 173 and r < 190):
				sys.stdout.write("??")
			elif(r > 189 and r < 206):
				sys.stdout.write("RR")
			elif(r > 205 and r < 222):
				sys.stdout.write("##")
			elif(r > 221 and r < 238):
				sys.stdout.write("$$")
			elif(r > 237 and r < 255):
				sys.stdout.write("QQ")
			else:
				sys.stdout.write("  ")
		print()			


#filtered_image = original.filter(ImageFilter.CONTOUR)

#filtered_image.save("new.bmp")

original.show()
