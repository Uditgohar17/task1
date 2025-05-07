from moviepy.editor import *
from TTS.api import TTS
import os

def create_video(script):
    os.makedirs("output", exist_ok=True)
    img = ImageClip("static/bg.jpg").set_duration(10)
    txt = TextClip(script, fontsize=24, color='white', size=img.size, method='caption').set_duration(10).set_position("center")
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
    tts.tts_to_file(text=script, file_path="output/audio.wav")
    audio = AudioFileClip("output/audio.wav")
    video = CompositeVideoClip([img, txt])
    video = video.set_audio(audio)
    video.write_videofile("output/final_video.mp4", fps=24)
    return "output/final_video.mp4"