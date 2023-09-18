class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagram):
        anagrams = []
        sorted_word = sorted(self.word)

        for words in possible_anagram:
            words = words.lower()

        
            if words != self.word and sorted(words) == sorted_word:
                anagrams.append(words)

        return anagrams

