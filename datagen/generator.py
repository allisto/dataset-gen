import os
import wave
import pylab as pl

i = 0


def graph_spectrogram(wav_file):
    global i 
    i = i + 1
    sound_info, frame_rate = get_wav_info(wav_file)
    pl.figure(num=None, figsize=(19, 12))
    pl.subplot(111)
    pl.title('spectrogram of %r' % wav_file)
    pl.specgram(sound_info, Fs=frame_rate)
    pl.savefig(os.getcwd() + '/images/spectrogram' + str(i))
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

for (dir, subdir, files) in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".wav"):
            graph_spectrogram(os.path.abspath("audio/" + file))


class DataGen:

    def __init__(self):
        self.file_count = 0
        self.img_path_save = '/images/spectogram'
        self.audio_path_save = 'audio/'
        self.figsize = (19,12)
        self.audio_format = '.wav'

    def gen_spectrogram(self, wav_file):
        self.file_count = self.file_count + 1
        self.sound_info, self.frame_rate = self.get_wave_info(wav_file)
        pl.figure(num=None, figsize=(19, 12))
        pl.subplot(111)
        pl.title('spectrogram of %r' % wav_file)
        pl.specgram(self.sound_info, Fs=self.frame_rate)
        pl.savefig(os.getcwd() + self.img_path_save + str(self.file_count))
    
    def get_wave_info(self, wav_file):
        self.wav = wave.open(wav_file, 'r')
        self.frames = self.wav.readframes(-1)
        self.sound_info = pl.fromstring(frames, 'int16')
        self.frame_rate = self.wav.getframerate()
        self.wav.close()
        return self.sound_info, self.frame_rate  
    
    def generate(self):
        for (dir, subdir, files) in os.walk(os.getcwd()):
            for file in files:
               if file.endswith(self.audio_format):
                    graph_spectrogram(os.path.abspath(self.audio_path_save + file))