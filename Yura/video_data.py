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



import imageio

video_path = "Yura/sample-10s.mp4"
num_frames = 10  # Number of frames to extract
interval = 0.1  # Time interval between frames (in seconds)

video = imageio.get_reader(video_path, 'ffmpeg')
fps = video.get_meta_data()['fps']
total_frames = video.get_length()
target_frames = min(num_frames, total_frames)  # Limit the number of frames to the total number of frames in the video

frames = []
frame_count = 0
current_time = 0.0

while frame_count < target_frames and current_time < total_frames / fps:
    frame_index = int(current_time * fps)
    frame = video.get_data(frame_index)
    frames.append(frame)
    frame_count += 1
    current_time += interval

video.close()

flat_frames = [frame.flatten() for frame in frames]
reshaped_frames = [frame.reshape(original_shape) for frame in flat_frames]
print(flat_frames)
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

