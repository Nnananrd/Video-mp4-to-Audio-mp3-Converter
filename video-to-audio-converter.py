import os
from moviepy.editor import VideoFileClip

def upload_video():
    while True:
        file_path = input("Enter the path to your MP4 video file: ")
        if os.path.isfile(file_path) and file_path.lower().endswith('.mp4'):
            return file_path
        else:
            print("Invalid file path or not an MP4 file. Please try again.")

def is_valid_video(file_path):
    try:
        with VideoFileClip(file_path) as video:
            # If we can read the video duration, it's likely a valid video file
            duration = video.duration
        return True
    except Exception as e:
        print(f"Error validating video: {str(e)}")
        return False

def convert_video_to_audio(video_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        return audio
    except Exception as e:
        print(f"Error converting video to audio: {str(e)}")
        return None

def is_valid_audio(audio):
    return audio is not None

def download_audio(audio, output_path):
    try:
        audio.write_audiofile(output_path)
        print(f"Audio saved successfully to {output_path}")
        return True
    except Exception as e:
        print(f"Error saving audio: {str(e)}")
        return False

def display_error_message(message):
    print(f"Error: {message}")

def main():
    while True:
        video_path = upload_video()
        
        if not is_valid_video(video_path):
            display_error_message("Invalid video file.")
            continue
        
        audio = convert_video_to_audio(video_path)
        
        if not is_valid_audio(audio):
            display_error_message("Failed to extract audio from video.")
            continue
        
        output_path = os.path.splitext(video_path)[0] + ".mp3"
        if download_audio(audio, output_path):
            print("Conversion completed successfully.")
            break
        else:
            display_error_message("Failed to save audio file.")

if __name__ == "__main__":
    main()
