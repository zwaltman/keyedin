#!/usr/bin/env python
"""
Classifiers for guessing key of pitch distribution.
"""

import pitchdistribution as pd
import numpy as np


class KrumhanslSchmuckler(object):
    """
    Classifier using the Krumhansl-Schmuckler key-finding algorithm.
    """
    def __init__(self):
        self.key_profiles = self.get_key_profiles()

    @staticmethod
    def get_key_profiles():
        """
        Return dictionary of typical pitch class distribution for all keys
        """
        profiles = {}
        for key in pd.NOTES:
            profiles[key] = pd.get_key_profile(key)
        return profiles

    def correlation(self, key, dist):
        """
        Given key KEY and pitch distribution DIST, return correlation coefficient of DIST and KEY's pitch profile
        """
        key_profile = self.key_profiles[key].to_array()
        data = np.array([dist, key_profile])
        return np.corrcoef(data)[1, 0]

    def get_key(self, dist):
        """
        Given pitch distribution DIST, return the key whose pitch profile best matches it
        """
        dist = dist.to_array()
        assert len(dist) == pd.NUM_NOTES, "Distribution must have %d notes, %d provided" % (pd.NUM_NOTES, len(dist))
        correlations = [self.correlation(key, dist) for key in pd.NOTES]
        return pd.NOTES[correlations.index(max(correlations))]
