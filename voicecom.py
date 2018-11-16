import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold = True
	print("say somthing!")
	audio = r.listen(source)


try:
	print(" you said: " + r.recognize_google(audio))
except sr.UnknowValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("could not request results from google Speech Recognition service; {0}".format(e))