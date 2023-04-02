from gtts import gTTS
import os
import pygame
from TranslatR_Validations import Validations

class Sounds:
    def __init__(self):
        pygame.mixer.init()
        self.validation_instance = Validations()

    def play_pronunciation(self, phrase, language):
        try:
            # print(phrase, language)

            # delete the music.mp3 file
            if os.path.exists('sound.mp3'):
                pygame.mixer.music.unload()
                os.remove('sound.mp3')

            myobj = gTTS(text=phrase, lang=language, slow=False)
            # # Saving the converted audio in a mp3 file named
            myobj.save("sound.mp3")

            # Playing the converted file
            # os.system("welcome.mp3")
            filename = 'sound.mp3'
            path = os.getcwd()
            self.sound = os.path.join(path, filename)

            pygame.mixer.music.load(self.sound)
            pygame.mixer.music.play()
        except:
            self.validation_instance.no_sound()

