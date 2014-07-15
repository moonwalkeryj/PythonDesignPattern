__author__ = 'Saturn'

'''
Adapter pattern works as a bridge between two incompatible interfaces.

This type of design pattern comes under structural pattern
    as this pattern combines the capability of two independent interfaces.

This pattern involves a single class
    which is responsible to join functionalities of independent or incompatible interfaces.

A real life example could be a case of card reader
    which acts as an adapter between memory card and a laptop.
You plugins the memory card into card reader and card reader into the laptop
        so that memory card can be read via laptop.

We are demonstrating use of Adapter pattern via following example
    in which an audio player device can play mp3 files only
    and wants to use an advanced audio player capable of playing vlc and mp4 files.

Implementation
    We've an interface MediaPlayer interface and a concrete class AudioPlayer implementing the MediaPlayer interface.
    AudioPlayer can play mp3 format audio files by default.

    We're having another interface AdvancedMediaPlayer and concrete classes implementing the AdvancedMediaPlayer interface.
    These classes can play vlc and mp4 format files.

    We want to make AudioPlayer to play other formats as well.
    To attain this, we've created an adapter class MediaAdapter which implements the MediaPlayer interface
        and uses AdvancedMediaPlayer objects to play the required format.

    AudioPlayer uses the adapter class MediaAdapter passing it the desired audio type
        without knowing the actual class which can play the desired format.
'''

class MediaPlayer:
    def play(self, type, filename):
        pass

class AdvancedMediaPlayer:
    def playMP4(self, filename):
        pass
    def playVLC(self, filename):
        pass

class MP4MediaPlayer(AdvancedMediaPlayer):
    def playMP4(self, filename):
        print "Playing MP4 ", filename

class VLCMediaPlayer(AdvancedMediaPlayer):
    def playVLC(self, filename):
        print "Playing VLC ", filename

class MediaAdapter(MediaPlayer):
    '''
    1. implement media player
    2. contain advanced media player the one we need to adapt to
    '''

    def __init__(self, type):
        if type == "MP4":
            self.advancedPlayer = MP4MediaPlayer()
        if type == "VLC":
            self.advancedPlayer = VLCMediaPlayer()

    def play(self, type, filename):
        if type == "MP4":
            self.advancedPlayer.playMP4(filename)
        if type == "VLC":
            self.advancedPlayer.playVLC(filename)

class AudioPlayer(MediaPlayer):

    def play(self, type, filename):
        if type == "MP4":
            MediaAdapter("MP4").play(type, filename)
        elif type == "VLC":
            MediaAdapter("VLC").play(type, filename)
        elif type == "MP3":
            print "Playing MP3 ", filename
        else:
            print "File Type not Support"

if "__main__" == __name__:
    audioplayer = AudioPlayer()
    audioplayer.play("MP4", "hello.mp4")
    audioplayer.play("VLC", "womendlfjsldjfla.vlc")
    audioplayer.play("MP3", "sldjflsdjfl.mp3")
    audioplayer.play("MP7", "heldsjfdsjllo.mp4")
