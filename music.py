import echonest.audio as audio

# Easy around wrapper mp3 decoding and Echo Nest analysis
audio_file = audio.LocalAudioFile("track.mp3")

# You can manipulate the beats in a song as a native python list
beats = audio_file.analysis.beats
beats.reverse()


# And render the list as a new audio file!
audio.getpieces(audio_file, beats).encode("track2.mp3")
