class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char, count in Counter(ransomNote).items():
            if Counter(magazine)[char] < count:
                return False
        return True
        