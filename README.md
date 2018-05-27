# keyedin

**Tool for distributional key-finding using Python.**

Identifies the most likely key of a musical audio recording from among the major and minor [diatonic scales](https://en.wikipedia.org/wiki/Diatonic_scale). Approximates the audio's [pitch class distribution](http://mp.ucpress.edu/content/25/3/193) using the [constant-Q transform](https://en.wikipedia.org/wiki/Constant-Q_transform), and then provides a variety of classifiers for guessing its key based on this distribution.

*[Note: The distributional view of tonality is well-known to be an incomplete picture of how the human auditory system identifies phenomena like 'key': It's an extreme abstraction which completely ignores structural information such as the order notes are heard in, which notes occur at the same time, etc. Despite this, in surprisingly many cases it allows for key-finding algorithms with acceptable accuracy. Google "distributional key-finding" or "pitch class distribution" for more info.]*

## Classifiers
### Krumhansl-Schmuckler
Uses a method based on the [Krumhansl-Schmuckler](http://rnhart.net/articles/key-finding/) key-finding algorithm to find a 'best fit' to a pitch class distribution. Compares the distribution to the 'typical' distribution for each key by taking their [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient), and then takes the argmax over these.

### Naive Bayes
Uses a [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) model wherein the audio's key is the class and the proportions of the audio made up by each note (i.e. the values of its pitch class distribution) are the features. 

### Others
Coming soon! The plan is to eventually include a classifier which uses a neural net (possibly just a multi-class perceptron), but first I need to figure out training data.

## Example Usage
```python
from keyedin import pitchdistribution as pd, classifiers

# Use naive Bayes classifier to guess the key of SongInGMajor.mp3
naive_bayes = classifiers.NaiveBayes()
dist = pd.PitchDistribution.from_file('path/to/SongInGMajor.mp3')
naive_bayes.get_key(dist) # Returns Key object Key('G', 'major')

# Use Krumhansl-Schmuckler classifier to guess the key of SongInBMinor.mp3
krumhansl_schmuckler = classifiers.KrumhanslSchmuckler()
dist = pd.PitchDistribution.from_file('path/to/SongInBMinor.mp3')
krumhansl_schmuckler.get_key(dist) # Returns Key object Key('B', 'minor')

# After key identification, tonal center and scale of keys are available through Key.get_tonic() and Key.get_scale
k = pd.Key('F', 'major')
k.get_tonic() # Returns string 'F'
k.get_scale() # Returns string 'major'
```

## Dependencies
* KeyedIn uses [Librosa](https://github.com/librosa) for its constant-Q transform implementation, which is required for Keyedin to work on any audio input. An installation guide for Librosa can be found [here](https://librosa.github.io/librosa/install.html).

* KeyedIn also uses [NumPy](https://github.com/numpy) for essential functions, so you'll need it too. Installation info for NumPy can be found [here](https://www.scipy.org/install.html).
