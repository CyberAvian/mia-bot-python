import pyttsx3
import speech_recognition as sr

class Bot():
    def __init__(self, voice=0):
        self.engine = pyttsx3.init()
        self.voice = self.set_voice(voice)
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def set_voice(self, voice_num):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice_num].id)
        # rate = self.engine.getProperty('rate')
        # self.engine.setProperty('rate', rate+25)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        try:
            with self.mic as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
            input = self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            input = ''
        return input

    def test_voices(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            print(voice, voice.id)
            self.engine.setProperty('voice', voice.id)
            self.speak('Hello world!')
            self.engine.runAndWait()


if __name__=='__main__':
    ts = Bot()
    ts.test_voices()
