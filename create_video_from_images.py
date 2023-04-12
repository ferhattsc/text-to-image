import cv2 
import os 
from os.path import isfile, join 

# Define a method that convert all output images to single video
def create_video_from_images_created(pathIn, pathOut, fps, time):

    frame_array=[]
    files=[f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]
    
    for i in range (len(files)):

        filename=pathIn+files[i]
        # Reading images
        img=cv2.imread(filename)

        # img=cv2.resize(img,(1400,1000))
        height, width, layers = img.shape
        size=(width,height)

        for k in range (time):

            frame_array.append(img)

    out=cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps,size)
   
    for i in range(len(frame_array)):

        out.write(frame_array[i])

    out.release()

