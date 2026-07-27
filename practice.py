import speech_recognition as sr

print(sr.__version__)
print([m for m in dir(sr.Recognizer()) if m.startswith("recognize")])

