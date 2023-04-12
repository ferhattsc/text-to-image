from googletrans import Translator
from create_video_from_images import *
from sleep_method import *

import shutil
import os

translator = Translator()
INPUT_TEXT = input("Type something that you want to convert an image: ")
result = translator.translate(INPUT_TEXT)
text = result.text

# Call the generate image method
generate_image(text)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Create params for Video Creat method
directory= './TextToImage/tree_in_the_sea'
pathIn=directory+'/'
pathOut=pathIn+'video_EX9.avi'
fps=10
time=1 # the duration of each picture in the video

## create_video_from_images_created(pathIn, pathOut, fps, time)


