from mutagen.easyid3 import EasyID3


class Player:
    def __init__(self, mp3_file):
        self.mp3_file = mp3_file
        pass

    def get_metadata(self):
        items = EasyID3(self.mp3_file).items()
        meta = '\n'.join(
            map(lambda kv: ''.join([kv[0], ": ", kv[1][0]]), items))
        return meta

    def play(self):
        pass

    def pause(self):
        pass

    def quit(self):
        pass
