
# Instalação: SpeechRecognition e PyAudio
# para pyaudio, digite no google "install pyaudio seu_sistema_operacional"
# Recognizer = Reconhece a voz
# microphone = Capitação da voz

import pyaudio
import speech_recognition as sr

rec = sr.Recognizer()
# print(sr.Microphone().list_microphone_names()) > Listar microfones no Desktop
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar...")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)


