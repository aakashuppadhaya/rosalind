from scipy import misc
import glob

for image_path in glob.glob("4e5e96caf3584de548ebac8a5dc703fd.png"):
    image = misc.imread(image_path)
    print(image.shape)
    print(image.dtype)
    print(image)
def crop_center(img,cropx,cropy):
	y,x = img.shape
	startx = x//2-(cropx//2)
	starty = y//2-(cropy//2)    
	return img[starty:starty+cropy,startx:startx+cropx]
img2=crop_center(image,4,6)
print(img2)