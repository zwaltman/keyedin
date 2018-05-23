#!/usr/bin/env python
"""
Class PitchDistribution represents proportion of musical sample made up of each note A, A#, B, ..., G, G#.
"""

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
INTERVALS = ['P1', 'm2', 'M2', 'm3', 'M3', 'P4', 'd5', 'P5', 'm6', 'M6', 'm7', 'M7']
NUM_NOTES = 12
# 'Prototypical' pitch distribution for major key with tonic A, adapted by rotating for use with any major key.
MAJOR_KEY_PROFILE = [0.16, 0.03, 0.09, 0.03, 0.13, 0.10, 0.06, 0.14, 0.03, 0.11, 0.03, 0.09]


def skip_interval(root, interval):
    """
    Returns note which is INTERVAL distance away from starting note ROOT.
    """
    assert root in NOTES, "Invalid note"
    assert interval in INTERVALS, "Invalid interval"
    starting_position = NOTES.index(root)
    distance = INTERVALS.index(interval)
    return NOTES[(starting_position + distance) % NUM_NOTES]


def get_key_profile(tonic):
    """
    Returns typical pitch distribution for major key centered at given tonic.
    """
    assert tonic in NOTES, "Invalid note"
    key_profile = PitchDistribution()
    for i in range(NUM_NOTES):
        current_note = skip_interval(tonic, INTERVALS[i])
        val = MAJOR_KEY_PROFILE[i]
        key_profile.set_val(current_note, val)
    return key_profile


class PitchDistribution(object):
    """
    Distribution over pitch classes A, A#, ..., G, G# in the form of a map NOTES --> [0,1]
    """
    def __init__(self, values=None):
        """
        Initializes empty distribution.
        """
        self.distribution = {}
        if values:
            assert len(values) == NUM_NOTES, "Distribution must have %d notes, %d provided" % (NUM_NOTES, len(values))
            for i in range(NUM_NOTES):
                note = NOTES[i]
                val = values[i]
                self.set_val(note, val)
            self.normalize()

    def __str__(self):
        return str([(note, self.get_val(note)) for note in NOTES])

    def to_array(self):
        return [self.get_val(note) for note in NOTES]

    def set_val(self, note, val):
        self.distribution[note] = float(val)

    def get_val(self, note):
        if note in self.distribution:
            return self.distribution[note]
        return 0.0

    def normalize(self):
        """
        Normalize distribution so that all entries sum to 1
        """
        distribution_sum = sum(self.distribution.values())
        if distribution_sum != 0:
            for k in self.distribution.keys():
                val = self.get_val(k)
                self.set_val(k, val / float(distribution_sum))
