class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagram):
        anagrams = []
        sorted_word = sorted(self.word)

        for letters in possible_anagram:
            letters = letters.lower()

        
            if letters != self.word and sorted(letters) == sorted_word:
                anagrams.append(letters)

        return anagrams

