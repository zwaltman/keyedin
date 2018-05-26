#!/usr/bin/env python
"""
Tests for keyedin package
"""

import pitchdistribution as pd
import classifiers
import unittest


class TestPitchDistribution(unittest.TestCase):

    def test_skip_interval_no_loop(self):
        actual = pd.skip_interval('B', 'm3')
        expected = 'D'
        self.assertEqual(actual, expected)

    def test_skip_interval_with_loop(self):
        actual = pd.skip_interval('G#', 'P5')
        expected = 'D#'
        self.assertEqual(actual, expected)

    def test_get_key_profile_sanity_check(self):
        actual = pd.get_key_profile('A').to_array()
        expected = pd.MAJOR_KEY_PROFILE
        self.assertEqual(actual, expected)

    def test_get_key_profile_with_loop(self):
        actual = pd.get_key_profile('F').to_array()
        expected = [0.13, 0.10, 0.06, 0.14, 0.03, 0.11, 0.03, 0.09, 0.16, 0.03, 0.09, 0.03]
        self.assertEqual(actual, expected)

    def test_pitch_distribution_sanity_check(self):
        values = [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        actual = pd.PitchDistribution(values).to_array()
        expected = [.1, 0, .1, 0, .1, .1, .1, .1, .1, .1, .1, .1]
        self.assertEqual(actual, expected)

    def test_pitch_distribution_get_set_vals(self):
        values = [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        dist = pd.PitchDistribution()
        for i in range(len(values)):
            dist.set_val(pd.NOTES[i], values[i])
        dist.normalize()
        expected = [.1, 0, .1, 0, .1, .1, .1, .1, .1, .1, .1, .1]
        for i in range(len(expected)):
            actual = dist.get_val(pd.NOTES[i])
            self.assertEqual(actual, expected[i])


class TestKrumhanslSchmucklerClassifier(unittest.TestCase):

    krumhansl_schmuckler = classifiers.KrumhanslSchmuckler()

    def test_monotonic_distribution(self):
        values = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        dist = pd.PitchDistribution(values)
        actual = self.krumhansl_schmuckler.get_key(dist)
        expected = 'E'
        self.assertEqual(actual, expected)

    def test_triad(self):
        values = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0]
        dist = pd.PitchDistribution(values)
        actual = self.krumhansl_schmuckler.get_key(dist)
        expected = 'C'
        self.assertEqual(actual, expected)

    def test_leading_tone(self):
        values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3]
        dist = pd.PitchDistribution(values)
        actual = self.krumhansl_schmuckler.get_key(dist)
        expected = 'G#'
        self.assertEqual(actual, expected)

    def test_add_4_triad(self):
        values = [2, 0, 0, 0, 3, 2, 0, 2, 0, 0, 0, 0]
        dist = pd.PitchDistribution(values)
        actual = self.krumhansl_schmuckler.get_key(dist)
        expected = 'A'
        self.assertEqual(actual, expected)

    def test_audio_file_in_F(self):
        dist = pd.PitchDistribution.from_filename('testaudio/RichGirl.mp3')
        actual = self.krumhansl_schmuckler.get_key(dist)
        expected = 'F'
        self.assertEqual(actual, expected)


class TestNaiveBayesClassifier(unittest.TestCase):

    naive_bayes = classifiers.NaiveBayes()

    def test_monotonic_distribution(self):
        values = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        dist = pd.PitchDistribution(values)
        actual = self.naive_bayes.get_key(dist)
        expected = 'E'
        self.assertEqual(actual, expected)

    def test_triad(self):
        values = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0]
        dist = pd.PitchDistribution(values)
        actual = self.naive_bayes.get_key(dist)
        expected = 'C'
        self.assertEqual(actual, expected)

    def test_leading_tone(self):
        values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3]
        dist = pd.PitchDistribution(values)
        actual = self.naive_bayes.get_key(dist)
        expected = 'G#'
        self.assertEqual(actual, expected)

    def test_add_4_triad(self):
        values = [2, 0, 0, 0, 3, 2, 0, 2, 0, 0, 0, 0]
        dist = pd.PitchDistribution(values)
        actual = self.naive_bayes.get_key(dist)
        expected = 'A'
        self.assertEqual(actual, expected)

    def test_audio_file_in_F(self):
        dist = pd.PitchDistribution.from_filename('testaudio/RichGirl.mp3')
        actual = self.naive_bayes.get_key(dist)
        expected = 'F'
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
