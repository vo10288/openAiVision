#!/usr/bin/python3

# by Antonio "Visi@n" Broi 
# http://www.broi.it/
# Version 0.3 Beta
# 20220604 H.17.00

#python2 reconMic.py -i lang -o lang 
# LICENSE M.I.T.              https://opensource.org/licenses/MIT
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
#OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
#OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import speech_recognition as sr
import argparse
import subprocess
from googletrans import Translator
import googletrans
from datetime import datetime
import pygame
pygame.init()
import time
from gtts import gTTS 
import os 


print(("""\

_____________________________________
( SPEECH TRANSLATE IN PYTHON BY              )
( VISI@N                              )
-------------------------------------
	""").encode('utf-8'))
     
print(("""\
__     ___     _   ____        
\ \   / (_)___(_) / __ \ _ __  
 \ \ / /| / __| |/ / _` | '_ \ 
  \ V / | \__ \ | | (_| | | | |
   \_/  |_|___/_|\ \__,_|_| |_|
                  \____/       
	""").encode('utf-8'))
    
print(("""\
	"Afrikaans": "South Africa", "af-ZA",
	"Arabic" : "Algeria","ar-DZ","Bahrain","ar-BH","Egypt","ar-EG","Israel","ar-IL","Iraq","ar-IQ","Jordan","ar-JO","Kuwait","ar-KW",
				"Lebanon","ar-LB","Morocco","ar-MA","Oman","ar-OM","Palestinian Territory","ar-PS","Qatar","ar-QA","Saudi Arabia","ar-SA",
				"Tunisia","ar-TN","UAE","ar-AE",
	"Basque": "Spain", "eu-ES",
	"Bulgarian": "Bulgaria", "bg-BG",
	"Catalan": "Spain", "ca-ES",
	"Chinese Mandarin": "China (Simp.)", "cmn-Hans-CN","Hong Kong SAR (Trad.)", "cmn-Hans-HK","Taiwan (Trad.)", "cmn-Hant-TW",
	"Chinese Cantonese": "Hong Kong", "yue-Hant-HK",
	"Croatian": "Croatia", "hr_HR",
	"Czech": "Czech Republic", "cs-CZ",
	"Danish": "Denmark", "da-DK",
	"English": "Australia", "en-AU","Canada", "en-CA","India", "en-IN","Ireland", "en-IE","New Zealand", "en-NZ","Philippines", "en-PH",
				"South Africa", "en-ZA","United Kingdom", "en-GB","United States", "en-US",
	"Farsi": "Iran", "fa-IR",
	"French": "France", "fr-FR",
	"Filipino": "Philippines", "fil-PH",
	"Galician": "Spain", "gl-ES","German": "Germany", "de-DE",
	"Greek": "Greece", "el-GR",
	"Finnish": "Finland", "fi-FI",
	"Hebrew" :"Israel", "he-IL",
	"Hindi": "India", "hi-IN",
	"Hungarian": "Hungary", "hu-HU",
	"Indonesian": "Indonesia", "id-ID",
	"Icelandic": "Iceland", "is-IS",
	"Italian": "Italy", "it-IT","Switzerland", "it-CH",
	"Japanese": "Japan", "ja-JP",
	"Korean": "Korea", "ko-KR",
	"Lithuanian": "Lithuania", "lt-LT",
	"Malaysian": "Malaysia", "ms-MY",
	"Dutch": "Netherlands", "nl-NL","Norwegian": "Norway", "nb-NO",
	"Polish": "Poland", "pl-PL",
	"Portuguese": "Brazil", "pt-BR","Portugal", "pt-PT",
	"Romanian": "Romania", "ro-RO",
	"Russian": "Russia", "ru-RU","Serbian": "Serbia", "sr-RS","Slovak": "Slovakia", "sk-SK","Slovenian": "Slovenia", "sl-SI",
	"Spanish": "Argentina", "es-AR","Bolivia", "es-BO","Chile", "es-CL","Colombia", "es-CO","Costa Rica", "es-CR","Dominican Republic", 
				"es-DO","Ecuador", "es-EC","El Salvador", "es-SV","Guatemala", "es-GT","Honduras", "es-HN","Mexico", "es-MX",
				"Nicaragua", "es-NI","Panama", "es-PA","Paraguay", "es-PY","Peru", "es-PE","Puerto Rico", "es-PR","Spain", "es-ES",
				"Uruguay", "es-UY","United States", "es-US","Venezuela", "es-VE",
	"Swedish": "Sweden", "sv-SE",
	"Thai": "Thailand", "th-TH",
	"Turkish": "Turkey", "tr-TR",
	"Ukrainian": "Ukraine", "uk-UA",
	"Vietnamese": "Viet Nam", "vi-VN",
	"Zulu": "South Africa", "zu-ZA"

	""").encode('utf-8'))

global timestampe
timestampe = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 


filename = timestampe
filestampe = timestampe


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-f", "--file", default=str(filename)+'.txt',#required=True,
	help="file were writing result")
ap.add_argument("-i", "--input", default="it",#required=True,
	help="input language")
ap.add_argument("-o", "--output", default="en",#required=True,
	help="output language")
	
args = vars(ap.parse_args())


if not os.path.exists('mp3'+str(args["input"])+'_'+str(args["output"])+timestampe):
	os.makedirs('mp3'+str(args["input"])+'_'+str(args["output"])+timestampe)    
if not os.path.exists('mp3ALL'+str(args["input"])+'_'+str(args["output"])+timestampe):
	os.makedirs('mp3ALL'+str(args["input"])+'_'+str(args["output"])+timestampe)   	
if not os.path.exists('txt'+str(args["input"])+'_'+str(args["output"])+timestampe):
	os.makedirs('txt'+str(args["input"])+'_'+str(args["output"])+timestampe)    
if not os.path.exists('txtALL'+str(args["input"])+'_'+str(args["output"])+timestampe):
	os.makedirs('txtALL'+str(args["input"])+'_'+str(args["output"])+timestampe)    



translator =  Translator()
id = 0

recognizer_instance = sr.Recognizer() # Create an instance of the recognizer
document = (args["file"])
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
		
#		rigatransARAA = translator.translate(test, dest="en")
#		rigatransARA = rigatransARAA.text.encode('utf8', 'replace')
#		comando = ('echo '+str(rigatransARA))
#		subprocess.Popen(comando, shell=True)
#		comando = ('say  '+'\"'+str(rigatransARA))+'\"'
#		subprocess.Popen(comando, shell=True)		
		
#		time.sleep(2)
		
#		rigatransARAE = translator.translate(test, dest="fr")
#		rigatransARE = rigatransARAE.text.encode('utf8', 'replace')
#		comando = ('echo '+str(rigatransARE))
#		subprocess.Popen(comando, shell=True)
#		comando = ('say '+'\"'+str(rigatransARE))+'\"'
#		subprocess.Popen(comando, shell=True)

		time.sleep(2)
				
		rigatransARAES = translator.translate(test, dest=str(args["output"])).text
		print(str(rigatransARAES))
		print('                                               ')
		#rigatransARAES = rigatransARAES[1:]
		rigatransARESS = rigatransARAES
		#rigatransARESS = rigatransARAES.text.encode('utf', 'replace')
		#rigatransARESS = rigatransARESS[1:]
		
#		comando = ('echo rigatransARESS : '+str(rigatransARESS))
#		subprocess.Popen(comando, shell=True)
		comando = ('say '+'\"'+str(rigatransARESS)+'\"')
#		comando = ('say '+str(rigatransARESS))
		subprocess.Popen(comando, shell=True)		

		time.sleep(2)
		
		id = id+1
		# Language in which you want to convert 
		language = str(args["output"])
		# have a high speed 
		myobj = gTTS(text=rigatransARESS, lang=language, slow=False) 
		# welcome  
		myobj.save('mp3'+str(args["input"])+'_'+str(args["output"])+filestampe+'/'+filename+str(id)+'.mp3') 
		# Playing the converted file 
		time.sleep(3)
#		os.system('mplayer "mp3'+str(args["input"])+'_'+str(args["output"])+filestampe+'/'+filename+str(id)+'.mp3')  
		
		comando = ('cat mp3'+str(args["input"])+'_'+str(args["output"])+filestampe+'/'+filename+str(id)+'.mp3 >> mp3ALL'+str(args["input"])+'_'+str(args["output"])+filestampe+'/'+str(args["input"])+'_'+str(args["output"])+'.mp3')
		subprocess.Popen(comando, shell=True)
		
				
#		speech.say(rigatransARA, 'ar_AR')  #WINDOWS
		
		documento = open('txt'+str(args["input"])+'_'+str(args["output"])+filestampe+'/'+document, "a")
		riga = (test)
		riga1 = (rigatransARESS)
		documento.write(riga)
		documento.write("\n")
		documento.write(riga1)
		documento.write("\n")


#		documento.write(rigatransARA)
#		documento.write("\n")
#		documento.write(rigatransARE)
#		documento.write("\n")
#		documento.write(rigatransARESS)
#		documento.write("\n")
		
		documento.write("===================== \n")
		
		
		documento.close()	
		
		################## txt ALL ############		
		documento = open('txtALL'+str(args["input"])+'_'+str(args["output"])+filestampe+'/'+str(args["input"])+'_'+str(args["output"])+'.txt', "a")
		riga = (test)
		riga1 = (rigatransARESS)
		documento.write(riga)
		documento.write("\n")
		documento.write(riga1)
		documento.write("\n")
#		documento.write(rigatransARE)
#		documento.write("\n")
#		documento.write(rigatransARESS)
#		documento.write("\n")
		
		documento.write("===================== \n")
		
		
		documento.close()

		
		id = int(id)
	except Exception as e:
		print(e)
exit
