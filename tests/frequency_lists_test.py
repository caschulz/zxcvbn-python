from unittest import TestCase

from zxcvbn.frequency_lists import FREQUENCY_LISTS


class TestRankedDictionaries(TestCase):
    def test_returns_dictionaries(self):
        assert isinstance(FREQUENCY_LISTS, dict)
        assert 'passwords' in FREQUENCY_LISTS
        assert 'english_wikipedia' in FREQUENCY_LISTS
        assert 'female_names' in FREQUENCY_LISTS
        assert 'surnames' in FREQUENCY_LISTS
        assert 'us_tv_and_film' in FREQUENCY_LISTS
        assert 'japanese_male_names' in FREQUENCY_LISTS
        assert 'japanese_female_names' in FREQUENCY_LISTS
        assert 'japanese_surnames' in FREQUENCY_LISTS
