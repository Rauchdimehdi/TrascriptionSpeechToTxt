import speech_recognition as sr

AUDIO_FILE = ("Test.wav")

r= sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source)

try:
	print("The Audio contains: " + r.recognize_google(audio) )

except sr.UnknownValueError:
	print("Google Speech failed ")

except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service")

