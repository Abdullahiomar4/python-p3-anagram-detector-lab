class Anagram:
    def __init__(self, word):
        # Store the word in lowercase for comparison purposes
        self.word = word.lower()

    def match(self, candidates):
        # Precompute the sorted letters of the original word
        sorted_word = sorted(self.word)
        
        # Check each candidate: compare lowercased and sorted, but return original casing
        return [
            candidate
            for candidate in candidates
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word
        ]
