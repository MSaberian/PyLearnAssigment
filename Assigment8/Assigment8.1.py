import os
import imageio

print(gtts.lang.tts_langs())

file_list = sorted(os.listdir('images'))

IMAGES = []
for file_name in file_list:
    file_path = 'images/' + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave('my_output.gif', IMAGES)
