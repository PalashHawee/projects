import sys
import os
from PIL import Image

#grab first and second argument
image_folder=sys.argv[1]
output_folder=sys.argv[2]
print(image_folder,output_folder)
#check if new is exist if not create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
#loop through pokedex folder
for filename in os.listdir(image_folder):
	img=Image.open(f'{image_folder}{filename}')
	clean_name=os.path.splitext(filename)
	print(clean_name)

	#img.save(f'{output_folder}{filename}.png','png')
	#print('all done!')
#convert images to png
#save to the new folder
