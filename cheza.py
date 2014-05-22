import pygame
import sys

from mutagen.easyid3 import EasyID3
from pydub import AudioSegment


class Song:
    def __init__(self, mp3_file):
        self.mp3_file = mp3_file
        self.duration = AudioSegment.from_mp3(mp3_file).duration_seconds
        self.pygame = pygame
        self.paused = None
        self.pygame.init()

    def get_metadata(self):
        items = EasyID3(self.mp3_file).items()
        items.append(['length', [str(self.duration)]])
        meta = '\n'.join(
            map(lambda kv: ''.join([kv[0].capitalize(), ": ", kv[1][0]]),
                items))
        return meta

    def play(self):
        self.pygame.mixer.music.load(self.mp3_file)
        self.pygame.mixer.music.play()

    def pause(self):
        self.pygame.mixer.music.pause()
        self.paused = True

    def unpause(self):
        self.pygame.mixer.music.unpause()
        self.paused = False

    def stop(self):
        self.pygame.mixer.stop()
        print "Kwaheri :-("
        sys.exit(0)
