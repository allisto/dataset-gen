import os
import wave
import pylab

i = 0


def graph_spectrogram(wav_file):
    global i 
    i = i + 1
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig(os.getcwd() + '/images/spectrogram' + str(i))
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