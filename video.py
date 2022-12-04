from moviepy.editor import *
import wave

def make_video(wav, thumb):
    with wave.open(wav) as w:
    # rounds number up to nearest second
        duration = round(w.getnframes() / w.getframerate())
        
    clips = []
    # image can be called anything just make sure to change file name as well as code
    img = ImageClip(thumb).set_duration(duration)
    
    clips.append(img)
    video = concatenate_videoclips(clips, method='compose')
    video.write_videofile('content/video.mp4', threads=8, fps=24, remove_temp=True, codec="libx264")
    
def add_audio(wav, video):
    clip = VideoFileClip(video)
    audio = AudioFileClip(wav)
    
    videoclip = clip.set_audio(audio)
    videoclip.write_videofile('content/beat.mp4', threads=8, fps=24, remove_temp=True, bitrate="5000k", audio=True, audio_codec="aac", codec="mpeg4")
