
import cv2 # pip install cv2
import moviepy.editor as mp # pip install moviepy
import numpy as np  # pip install np
import os
import tqdm # # pip install tqdm


#Video location
video = os.getcwd() + "/test.mp4"

# Load the video clip
clip = mp.VideoFileClip(video)

# Set start and end time
start_time = "00:00"
end_time = "0:05"

# Cut the video to a specific duration (in seconds)
cut_clip = clip.subclip(start_time, end_time)

# Resolutions 
quad_hd_w = 2560
quad_hd_h = 1440
quad_hd_h_2 = 1600

four_k_w = 3840
four_k_h = 2160

# Increase the resolution of the video
upscaled_clip = cut_clip.resize(width = four_k_w, height = four_k_h)

# Improve the brightness of the video
brightened_clip = upscaled_clip.fx(mp.vfx.colorx, 1.5)

# Save the modified video
brightened_clip.write_videofile("modified.mp4")

# Iterate through the frames, sharpened them and then save them to a folder in the current working directory
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

for i, frame in enumerate(brightened_clip.iter_frames()):
    sharpened_frame = cv2.filter2D(frame, -1, kernel)
    cv2.imwrite(f"frames/frame{i}.jpg", sharpened_frame)
