from mutagen.easyid3 import EasyID3
from pydub import AudioSegment


class Player:
    def __init__(self, mp3_file):
        self.mp3_file = mp3_file
        self.song_duration = AudioSegment.from_mp3(mp3_file).duration_seconds

    def get_metadata(self):
        items = EasyID3(self.mp3_file).items()
        items.append(['length', [str(self.song_duration)]])
        meta = '\n'.join(
            map(lambda kv: ''.join([kv[0].capitalize(), ": ", kv[1][0]]),
                items))
        return meta

    def play(self):
        pass

    def pause(self):
        pass

    def quit(self):
        pass
