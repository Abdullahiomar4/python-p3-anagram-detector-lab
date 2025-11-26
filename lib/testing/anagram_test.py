import pytest
from lib.anagram import Anagram

def test_no_matches():
    word = Anagram("diaper")
    assert word.match(["hello", "world", "zombies", "pants"]) == []

def test_detects_anagram():
    word = Anagram("listen")
    assert word.match(["enlists", "google", "inlets", "banana"]) == ["inlets"]

def test_does_not_confuse_identical_words():
    word = Anagram("corn")
    # Should not match itself, even with different casing
    assert word.match(["corn", "dark", "Corn", "rank", "CORN"]) == []

def test_multiple_anagrams():
    word = Anagram("allergy")
    # Only true anagrams: letters must match exactly
    assert set(word.match(["gallery", "ballerY", "regally", "clergy"])) == set(["gallery", "regally"])
