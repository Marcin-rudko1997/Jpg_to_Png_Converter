import os
import sys
from PIL import Image

images_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)
    print(f'folder {destination_folder} was successfully created')
else:
    print(f'folder {destination_folder} already exists!')


for filename in os.listdir(images_folder):
    if filename.endswith('jpg'):
        img = Image.open(f'{images_folder}{filename}')
        name = os.path.splitext(filename)[0]
        img.save(f'{destination_folder}{name}.png')
