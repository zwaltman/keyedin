# keyedin

Tool for distributional key-finding written in Python.

Identifies the most likely key of a musical audio recording by approximating its pitch class distribution using fast Fourier transform methods, then using a method based on the [Krumhansl-Schmuckler](http://rnhart.net/articles/key-finding/) key-finding algorithm to find a 'best fit' to this distribution from among the major and natural minor diatonic scales. (I plan to eventually replace Krumhansl-Schmuckler with supervised learning, once I figure out training data.)
