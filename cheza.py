#!/usr/bin/env python

import pygame
import sys

from mutagen.easyid3 import EasyID3
from pydub import AudioSegment
from clint import textui
from time import sleep


class Song:
    def __init__(self, mp3_file):
        self.mp3_file = mp3_file
        self.duration = int(AudioSegment.from_mp3(mp3_file).duration_seconds)
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
        sys.exit(0)

    def toggle_pause(self):
        if not self.paused:
            self.pause()
        else:
            self.unpause()

if __name__ == '__main__':
    song_file = sys.argv[1]
    song = Song(song_file)
    progress_bar = textui.progress.bar(range(song.duration))
    try:
        print textui.colored.blue("Cheza Media Player")
        print textui.colored.blue("Karibu")
        print textui.colored.green(song.get_metadata())
        progress_bar.send(None)
        song.play()
        while song.pygame.mixer.music.get_busy():
            sleep(1)
            progress_bar.send(int(song.pygame.mixer.music.get_pos())/1000)
    except KeyboardInterrupt:
        progress_bar.close()
        print ''
        print textui.colored.red("Kwaheri :-(")
        song.stop()
