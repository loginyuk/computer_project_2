import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate
import os
from PIL import Image
import shutil
from algorithms import *

from image_data import work_with_image
from audio_data import work_with_audio

def video_to_string(video_file: str) -> str:
    # video_file = 'sample-10s.mp4'  # Path to the video file

    video_clip = VideoFileClip(video_file)

    fps = video_clip.fps

    audio = video_clip.audio
    audio.write_audiofile('files/video_audio.mp3')
    audio_file = 'files/video_audio.mp3'  # Path to the audio file
    audio_clip = AudioFileClip(audio_file)              

    frame_rate = 30  # Sample every 10 frames

    # чистить папку і створює нову
    output_folder = 'files/frames'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(file_path):
            # Remove the file
            os.remove(file_path)
    os.rmdir(output_folder)
    os.makedirs(output_folder)


    # робить array з фото
    sampling_data = []
    for frame_number, frame in enumerate(video_clip.iter_frames()):
        if frame_number % int(fps) == 0:
            sampling_data.append(frame)



    # записує фото в папку
    for i, frame in enumerate(sampling_data):
        frame_path = os.path.join(output_folder, f"frame_{i}.jpg")
        image = Image.fromarray(frame)
        image.save(frame_path)

    return audio_file, output_folder, fps, video_clip, audio_clip

def video_back(fps, video_clip, audio_clip, path):
    video_clip = concatenate([video_clip.resize((video_clip.size[0], video_clip.size[1])).loop(duration=audio_clip.duration)])
    video_clip = video_clip.set_audio(audio_clip)
    # path = os.path.abspath(path)
    new_path = 'video.mp4'
    # shutil.move(path, '/Users/loginuha/op/discrete/computer_project_2/cmp_2'+path.split('/')[-1])
    video_clip.write_videofile(new_path, codec='libx264', audio_codec='aac', fps=fps)
    os.rename(new_path, path)



def work_with_video(path, algorithm):
    data_from_video = video_to_string(path)
    statistics_audio = work_with_audio(data_from_video[0], algorithm)
    statistics_frames = []
    for i in range(len(os.listdir(data_from_video[1]))):
        statistics_frames += work_with_image(f'files/frames/frame_{i}.jpg', algorithm)

    # [compression_ratio, compress_time, decompress_time]

    statistics_photo = [statistics_frames[0]]
    for i in statistics_frames:
        statistics_photo[1] += i[0]
        statistics_photo[2] += i[1]
        statistics_photo[3] += i[2]
    for i in statistics_photo:
        statistics_photo[i] /= len(statistics_frames)
    
    statistics = [statistics_photo[0] + statistics_audio[0], statistics_photo[1] + statistics_audio[1], statistics_photo[2] + statistics_audio[2]]




    video_back(data_from_video[2], data_from_video[3], data_from_video[4], path)
    output_folder = 'files/frames'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(file_path):
            # Remove the file
            os.remove(file_path)
    os.rmdir(output_folder)
    return statistics











# from moviepy.editor import VideoFileClip
# import numpy as np

# video = VideoFileClip('Yura/video.mp4')

# # Extract the audio from the video
# audio = video.audio

# # Convert the audio to a mono channel
# # audio = audio.set_channels(1)

# # Get the raw audio data as a NumPy array
# audio_data = audio.to_soundarray()

# # Flatten the audio data if it has multiple channels
# if audio_data.ndim > 1:
#     audio_data = np.mean(audio_data, axis=1)

# # Normalize the audio data if desired
# # audio_data /= np.max(np.abs(audio_data))

# # Print the shape of the audio data
# print(audio_data)







# from moviepy.editor import VideoFileClip
# import librosa

# video = VideoFileClip('Yura/video.mp4')

# # Extract the audio from the video
# audio = video.audio

# # Extract the audio data as a NumPy array
# audio_data = audio.to_soundarray()

# # Convert the audio to mono using librosa
# mono_audio_data = librosa.to_mono(audio_data.T)

# # Print the shape of the mono audio data
# print(mono_audio_data)



# import cv2
# import numpy as np
# video = cv2.VideoCapture('sample-10s.mp4')

# sampling_data = []
# while video.isOpened():
#     ret, frame = video.read()
#     if not ret:
#         break

#     # Process the frame or extract the desired information
#     # For example, convert to grayscale:
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Append the sampling data to the list
#     sampling_data.append(gray_frame)

# # Convert the list to a NumPy array
# sampling_data = np.array(sampling_data)








# from cv2 import cv2
# from moviepy.editor import VideoFileClip
# video_path = "sample-10s.mp4"
# video = VideoFileClip(video_path)
# audio_path = "video_wav.wav"
# video.audio.write_audiofile(audio_path)


# video = cv2.VideoCapture(video_path)
# frame_path = "output_frames/frame"
# frame_count = 0

# while video.isOpened():
#     ret, frame = video.read()

#     if not ret:
#         break

#     cv2.imwrite(frame_path + str(frame_count) + ".jpg", frame)
#     frame_count += 1

# video.release()



# import imageio

# video_path = "Yura/sample-10s.mp4"
# num_frames = 10  # Number of frames to extract
# interval = 0.1  # Time interval between frames (in seconds)

# video = imageio.get_reader(video_path, 'ffmpeg')
# fps = video.get_meta_data()['fps']
# total_frames = video.get_length()
# target_frames = min(num_frames, total_frames)  # Limit the number of frames to the total number of frames in the video

# frames = []
# frame_count = 0
# current_time = 0.0

# while frame_count < target_frames and current_time < total_frames / fps:
#     frame_index = int(current_time * fps)
#     frame = video.get_data(frame_index)
#     frames.append(frame)
#     frame_count += 1
#     current_time += interval

# video.close()

# flat_frames = [frame.flatten() for frame in frames]
# reshaped_frames = [frame.reshape(original_shape) for frame in flat_frames]
# print(flat_frames)
# import matplotlib.pyplot as plt
# # print(len(frames[0][0][0]))
# import imageio

# image_path = "path_to_image.png"

# image = imageio.imread(image_path)
# image_list = image.tolist()

# print(image_list)

# Do further processing with the extracted frames
# for frame in frames:
#     # Perform operations on each frame as desired
#     plt.imshow(frame)
#     plt.axis('off')
#     plt.show()





# import cv2

# def extract_frames(video_path, output_folder, frame_interval):
#     # Open the video file
#     video = cv2.VideoCapture(video_path)
    
#     # Initialize frame counter
#     frame_count = 0
    
#     while True:
#         # Read a frame from the video
#         ret, frame = video.read()
        
#         # If frame reading was successful
#         if ret:
#             # Save the frame at the desired interval
#             if frame_count % frame_interval == 0:
#                 frame_path = f"{output_folder}/frame_{frame_count}.jpg"
#                 cv2.imwrite(frame_path, frame)
            
#             frame_count += 1
#         else:
#             break
    
#     # Release the video object
#     video.release()

# # Example usage
# video_path = "path/to/video.mp4"
# output_folder = "path/to/output/folder"
# frame_interval = 10  # Save every 10th frame

# extract_frames(video_path, output_folder, frame_interval)




# from moviepy.editor import VideoFileClip
"""
тут добре записує відео, але без звуку
"""
# import numpy as np
# from moviepy.audio.io.AudioFileClip import AudioFileClip
# import moviepy.editor

# video = moviepy.editor.VideoFileClip('sample-10s.mp4')
# frame_rate = 30  # Sample every 10 frames
# sampling_data = []
# for frame_number, frame in enumerate(video.iter_frames()):
#     if frame_number % frame_rate == 0:
#         sampling_data.append(frame)
# sampling_data = np.array(sampling_data)
# video_out = video.set_fps(frame_rate)
# video_out.write_videofile('new_video.mp4')
# video_with_audio = video.set_fps(frame_rate)
# audio = video.audio
# audio.write_audiofile('video_audio.mp3')
# audio_au = AudioFileClip('video_audio.mp3')



# import os
# from moviepy.editor import ImageSequenceClip

# sampling_data_filtered = [path for path in sampling_data if '\0' not in path]
# video_with_audio = ImageSequenceClip(sampling_data_filtered, fps=frame_rate)

# video_with_audio = video_with_audio.set_audio(audio_au)
# video_with_audio.write_videofile('new_video.mp4')
# video_out.write_videofile('new_video.mp4')



""""
тут добре записує аудіо в відео
"""
# import numpy as np
# from moviepy.editor import ImageSequenceClip, AudioFileClip

# audio_file = 'video_audio.mp3'  # Path to the audio file
# frame_rate = 30  # Sample every 10 frames
# sampling_data = []
# for frame_number, frame in enumerate(video.iter_frames()):
#     if frame_number % frame_rate == 0:
#         sampling_data.append(frame)
# sampling_data = np.array(sampling_data)
# video_clip = ImageSequenceClip(list(sampling_data), fps=frame_rate)
# audio_clip = AudioFileClip(audio_file)
# video_clip = video_clip.set_audio(audio_clip)
# output_file = 'new_videot.mp4'
# video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')



################################################################################################################################
# import numpy as np
# from moviepy.editor import VideoFileClip, AudioFileClip, concatenate
# import os
# from PIL import Image

# video_file = 'sample-10s.mp4'  # Path to the video file

# video_clip = VideoFileClip(video_file)

# fps = video_clip.fps

# audio = video_clip.audio
# audio.write_audiofile('video_audio.mp3')
# audio_au = AudioFileClip('video_audio.mp3')
# audio_file = 'video_audio.mp3'  # Path to the audio file
# audio_clip = AudioFileClip(audio_file)

# frame_rate = 30  # Sample every 10 frames

# # чистить папку і створює нову
# output_folder = 'frames'
# for filename in os.listdir(output_folder):
#     file_path = os.path.join(output_folder, filename)
#     # Check if the file is a regular file (not a directory)
#     if os.path.isfile(file_path):
#         # Remove the file
#         os.remove(file_path)
# os.rmdir(output_folder)
# os.makedirs(output_folder)


# # робить array з фото
# sampling_data = []
# for frame_number, frame in enumerate(video_clip.iter_frames()):
#     if frame_number % int(fps) == 0:
#         sampling_data.append(frame)
# print(len(sampling_data))


# # записує фото в папку
# for i, frame in enumerate(sampling_data):
#     frame_path = os.path.join(output_folder, f"frame_{i}.jpg")
#     image = Image.fromarray(frame)
#     image.save(frame_path)



# # 
# video_clip = concatenate([video_clip.resize((video_clip.size[0], video_clip.size[1])).loop(duration=audio_clip.duration)])
# video_clip = video_clip.set_audio(audio_clip)
# output_file = 'new_video.mp4'
# video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=fps)












################################################################################################################################
# from moviepy.editor import AudioFileClip, VideoClip
# import numpy as np

# audio_file = 'video_audio.mp3'  # Path to the audio file
# frame_rate = 30  # Desired frame rate (sampling rate)

# # Load the audio clip
# audio_clip = AudioFileClip(audio_file)

# # Calculate the duration of the audio clip
# audio_duration = audio_clip.duration

# # Specify the frame size for the blank video clip
# frame_width = 1280  # Adjust the width as needed
# frame_height = 720  # Adjust the height as needed
# frame_size = (frame_width, frame_height)

# # Create a blank video clip with the specified size and duration
# blank_frame = VideoClip(make_frame=lambda t: np.zeros(frame_size + (3,)), duration=audio_duration)

# # Set the frame rate of the blank video clip
# blank_frame = blank_frame.set_fps(frame_rate)

# # Set the audio of the blank video clip to the loaded audio clip
# video_clip = blank_frame.set_audio(audio_clip)

# # Specify the output file name
# output_file = 'new_video.mp4'

# # Write the video file with the desired frame rate
# video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=frame_rate)

# print("New video created successfully.")
