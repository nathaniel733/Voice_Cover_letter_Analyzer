from moviepy.editor import VideoFileClip

def extract_audio(video_path):
    # Load video
    clip = VideoFileClip(video_path)
    
    # Define output path for the audio file
    audio_path = video_path.replace(".mp4", ".wav")
    
    # Extract and write audio
    clip.audio.write_audiofile(audio_path)
    
    return audio_path
