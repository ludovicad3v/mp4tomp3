import sys
import os
from moviepy.editor import VideoFileClip


def extract_audio(video_path, audio_output_path):
    try:
        with VideoFileClip(video_path) as video:
            audio = video.audio
            audio.write_audiofile(audio_output_path)
    except Exception as e:
        print(f"Error extracting audio: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Usage: python cnvrt.py <video_file_path> <destination_folder>")
        sys.exit(1)

    video_path = sys.argv[1]
    destination_folder = sys.argv[2]

    if not os.path.isfile(video_path):
        print(f"Error: Video file '{video_path}' does not exist.")
        sys.exit(1)

    if not os.path.isdir(destination_folder):
        print(f"Error: Destination folder '{destination_folder}' does not exist.")
        sys.exit(1)

    file_name = os.path.splitext(os.path.basename(video_path))[0] + ".mp3"
    audio_output_path = os.path.join(destination_folder, file_name)

    extract_audio(video_path, audio_output_path)
    print(f"Audio extracted and saved to '{audio_output_path}'")


if __name__ == "__main__":
    main()
