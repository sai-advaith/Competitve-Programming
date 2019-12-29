class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for ch in arr:
            dict[ch] = dict.get(ch,0) + 1
        return (len(set(dict.values())) == len(dict.values()))