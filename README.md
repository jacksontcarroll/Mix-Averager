# Mix Averager
### Idea
- Web application where an original audio file is uploaded, then the user can upload multiple edited versions (mixes, masters, etc.) The application will do some DSP in Python behind the scenes, then spit out an "average" mix or master based on the changes to each frequency in each version.
- I hypothesize that, similarly to how the average guesses of many people guessing how many beans are in a jar are much closer to the actual amount than any individual guess, the average mix or master compiled from many different mixes or masters will be viewed as a more "correct" mix by audio professionals.

### Progression
- [ ] Create a web application that can read in files and send them to a Python script utilizing the libraries I need -- likely numpy, potentially others
- [ ] Get a working prototype: 1 base audio file and 2 mixed, program should phase invert the original, perform an FFT on the resulting sums, average each frequency change, then re-add each frequency to the base audio (FFT the base audio file and sum in the frequency spectrum)
- [ ] Improve the prototype to work with any number of mixes
- [ ] Incorporate discrete STFT for an arbitrary time resolution
- [ ] Improve web application to allow the user to experiment with different time resolutions
- [ ] Add tempo-tracking to set the time resolution to the tempo of the song (every measure / beat)
