import openai
import re
from api_key import API_KEY
import time
import subprocess
from datetime import datetime
### audio
import speech_recognition as sr
from gtts import gTTS 
import os 


### translate
from googletrans import Translator
import googletrans


## argparse
import argparse

datatimestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
	
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-f", "--file", default=str(datatimestamp)+".txt",#required=True,
	help="file were writing result")
ap.add_argument("-i", "--input", default="it",#required=True,
	help="input language")
ap.add_argument("-o", "--output", default="en",#required=True,
	help="output language")
	
args = vars(ap.parse_args())

#Create Necessary Folders
if not os.path.exists("CHATONLY"):
	os.makedirs("CHATONLY")






openai.api_key = API_KEY

# Set the model to use
model_engine = "text-davinci-003"

#######################################################
#recognize audio from microphone


translator =  Translator()
id = 0

recognizer_instance = sr.Recognizer() # Create an instance of the recognizer
#document = (args["file"])
#while True:
while True:
	with sr.Microphone() as source:
		recognizer_instance.adjust_for_ambient_noise(source)
		print("I'm listening ... speak well!")
		audio = recognizer_instance.listen(source)
		print("Ok! I am now processing the message!")
	try:
		test = recognizer_instance.recognize_google(audio, language=str(args["input"]))
	#		tests = tests.encode('utf8', 'replace')
		print("OK ... audio reconnaissance in progress....: \n", str(test))
	########################################################
	# translate in English


		time.sleep(2)
		command = ('say '+str(test))
		subprocess.Popen(command, shell=True)	

				
		rigatranslate = translator.translate(test, dest=str(args["output"])).text
		print(str(rigatranslate))
		print('                                               ')
		time.sleep(2)
	
		command = ('say '+str(rigatranslate))
		subprocess.Popen(command, shell=True)	
		time.sleep(2)





#######################################################

	# Set the prompt to generate text for
	#text = input("What topic you want to write about: ")
		prompt = rigatranslate

		print("The AI BOT is trying now to generate a new text for you...")
		# Generate text using the GPT-3 model
		completions = openai.Completion.create(
			engine=model_engine,
			prompt=prompt,
			max_tokens=1024,
			n=1,
			stop=None,
			temperature=0.5,
		)

		# Print the generated text
		generated_text = completions.choices[0].text
		print('%%%%%%%%%%%%%%%%%%%%%%%')
		print(str(generated_text))
		print('                                               ')

		print('%%%%%%%%%%%%%%%%%%%%%%%')
	
		time.sleep(1)
		rigatranslateIT = translator.translate(generated_text, dest=str(args["input"])).text
		print(str(rigatranslateIT))
		print('                                               ')
		time.sleep(4)
	
		# Save the text in a file
		with open('CHATONLY/EN'+str(args["file"]), "a") as file:
			file.write(rigatranslate.strip())
		time.sleep(2)	
		
		with open('CHATONLY/EN'+str(args["file"]), "a") as file:
			file.write('\\n$$$$$$$$$$$$$$$$$$$$\\n')
		time.sleep(2)	
		
		with open('CHATONLY/EN'+str(args["file"]), "a") as file:
			file.write(generated_text.strip())
		time.sleep(2)
		
		with open('CHATONLY/EN'+str(args["file"]), "a") as file:
			file.write('\\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\\n')
		time.sleep(2)	
			
		print('%%%%%%%%%%%%%%%%%%%%%%%')
	
		#time.sleep(3)
	#	command = ('cat CHATONLY/EN'+str(args["file"])+'| say ')
	#	subprocess.Popen(command, shell=True)
	#	time.sleep(4)
	
	
		with open('CHATONLY/IT'+str(args["file"]), "a") as file:
			file.write(test.strip())
		time.sleep(2)	
		with open('CHATONLY/IT'+str(args["file"]), "a") as file:
			file.write('\\n$$$$$$$$$$$$$$$$$$$$\\n')
		time.sleep(2)
		
		with open('CHATONLY/IT'+str(args["file"]), "a") as file:
			file.write(rigatranslateIT.strip())
		time.sleep(2)	
		with open('CHATONLY/IT'+str(args["file"]), "a") as file:
			file.write('\\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\\n')
		time.sleep(2)	
			
		print('%%%%%%%%%%%%%%%%%%%%%%%')
		
		with open('CHATONLY/'+str(args["file"]), "w") as file:
			file.write(rigatranslateIT.strip())
		time.sleep(2)	
		
		command = ('cat CHATONLY/'+str(args["file"])+'| say ')
		subprocess.Popen(command, shell=True)
		time.sleep(70)
	
		print("The Text Has Been Generated Successfully!")
	except:
		print('Houston there is a probem!! a big problem!!!')	


#time.sleep(2)

#command = ('python video_generator4translateIT.py')
#subprocess.Popen(command, shell=True)
#time.sleep(120)
	
