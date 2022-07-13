import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Import the audio files
data_base, sr_base = sf.read('aud/flute.wav')
data_mix1, sr_mix1 = sf.read('aud/mix1.wav')
data_mix2, sr_mix2 = sf.read('aud/mix2.wav')

# Get the FFTs of the base audio file as well as of the
# difference between each mix and the base (just the frequencies
# affected during mixing)
base_freq = np.fft.fft(data_base)
mix1_diff_freq = np.fft.fft(data_mix1 - data_base)
mix2_diff_freq = np.fft.fft(data_mix2 - data_base)

# Take the average of the difference in frequencies (in the freq domain)
avg_diff_freq = (mix1_diff_freq + mix2_diff_freq) / 2

# Take the inverse transform to get it back to the time domain
avg_diff_time = np.fft.ifft(base_freq + avg_diff_freq).real

# Write our file!
sf.write('avg_mix.wav', avg_diff_time, sr_base)
