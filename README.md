# keyedin

**Tool for distributional key-finding using Python.**

Identifies the most likely key of a musical audio recording from among the major and minor [diatonic scales](https://en.wikipedia.org/wiki/Diatonic_scale). Approximates the audio's [pitch class distribution](http://mp.ucpress.edu/content/25/3/193) using fast Fourier transform methods, and then provides a variety of classifiers for guessing its key based on this distribution.

*[The distributional view of tonality is well-known to be an incomplete picture of how the human auditory system identifies phenomena like 'key': It's an extreme abstraction which completely ignores structural information such as the order notes are heard in, which notes occur at the same time, etc. Despite this, in surprisingly many cases it allows for key-finding algorithms with acceptable accuracy. Google "distributional key-finding" or "pitch class distribution" for more info.]*

## Classifiers
### Krumhansl-Schmuckler
Uses a method based on the [Krumhansl-Schmuckler](http://rnhart.net/articles/key-finding/) key-finding algorithm to find a 'best fit' to a pitch class distribution. Compares the distribution to the 'typical' distribution for each key by taking their [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient), and then takes the argmax over these.

### Naive Bayes
Uses a [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) model wherein the audio's key is the class and the proportions of the audio made up by each note (i.e. the values of its pitch class distribution) are the features. 

### Others
Coming soon! The plan is to eventually include a classifier which uses a neural net (possibly just a multi-class perceptron), but first I need to figure out training data.
