class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #order doesn't matter. 
        #hashmap to track characters?
        #if all characters are in hashmap return true?

        freq_s = {}
        freq_t = {}

        for i in s:
            freq_s[i] = freq_s.get(i, 0) + 1

        
        for j in t:
                freq_t[j] = freq_t.get(j, 0) + 1


        return freq_s == freq_t




