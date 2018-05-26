#!/usr/bin/env python
"""
Tools for processing audio data
"""

import librosa
import librosa.display


def chromagram_from_filename(filename):
    """
    Takes path FILENAME to audio file and returns the file's chromagram C (numpy array with shape=(12, t=num_time_samples))
    """
    y, sr = librosa.load(filename)
    # Separate harmonic component from percussive
    y_harmonic = librosa.effects.hpss(y)[0]
    # Make CQT-based chromagram using only the harmonic component to avoid pollution
    C = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
    return C
