class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr_string = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in arr_string:
                arr_string[key].append(s)
            else:
                arr_string[key] = [s]
        
        return list(arr_string.values())
        