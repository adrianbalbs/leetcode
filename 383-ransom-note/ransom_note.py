import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteLetters = collections.Counter()
        magazineLetters = collections.Counter()

        for c in ransomNote:
            ransomNoteLetters[c] += 1
        for c in magazine:
            magazineLetters[c] += 1

        for key, val in ransomNoteLetters.items():
            if key not in magazineLetters or val > magazineLetters[key]:
                return False

        return True
