import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate
from PIL import Image

from algorithms import *
from image_data import work_with_image
from audio_data import work_with_audio

def video_to_string(video_file: str) -> str:
    """
    Make audio from video
    Make photos from video
    """
    video_clip = VideoFileClip(video_file)
    fps = video_clip.fps
    audio = video_clip.audio
    audio.write_audiofile('files/video_audio.mp3')
    audio_file = 'files/video_audio.mp3'
    audio_clip = AudioFileClip(audio_file)

    # clear folder and make new
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

    sampling_data = []
    for frame_number, frame in enumerate(video_clip.iter_frames()):
        if frame_number % int(fps) == 0:
            sampling_data.append(frame)

    # make photos
    for i, frame in enumerate(sampling_data):
        frame_path = os.path.join(output_folder, f"frame_{i}.jpg")
        image = Image.fromarray(frame)
        image.save(frame_path)

    return audio_file, output_folder, fps, video_clip, audio_clip


def video_back(fps, video_clip, audio_clip, path):
    """
    Make video from audio and photos
    """
    video_clip = concatenate([video_clip.resize((video_clip.size[0],\
                video_clip.size[1])).loop(duration=audio_clip.duration)])
    video_clip = video_clip.set_audio(audio_clip)
    new_path = 'video.mp4'
    video_clip.write_videofile(new_path, codec='libx264', audio_codec='aac', fps=fps)
    os.rename(new_path, path)


def work_with_video(path, algorithm):
    """
    Works with video file
    """
    statistics_frames = []
    data_from_video = video_to_string(path)
    statistics_audio = work_with_audio(data_from_video[0], algorithm)
    for i in range(len(os.listdir(data_from_video[1]))):
        statistics_frames.append(work_with_image(f'files/frames/frame_{i}.jpg', algorithm))
    # [[compression_ratio, compress_time, decompress_time], [], [], []]
    
    statistics_photo = list(statistics_frames[0])
    print(statistics_photo)
    for i in statistics_frames:
        statistics_photo[0] += i[0]
        statistics_photo[1] += i[1]
        statistics_photo[2] += i[2]
    for i, _ in enumerate(statistics_photo):
        statistics_photo[i] = statistics_photo[i]/len(statistics_frames)
    statistics = [statistics_photo[0] + statistics_audio[0],\
            statistics_photo[1] + statistics_audio[1], statistics_photo[2] + statistics_audio[2]]

    output_folder = 'files/frames'
    video_back(data_from_video[2], data_from_video[3], data_from_video[4], path)
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
