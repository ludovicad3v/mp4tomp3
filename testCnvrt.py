try:
    from moviepy.editor import VideoFileClip
    print("moviepy imported successfully!")
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")
