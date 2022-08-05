from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordCount = len(words)
        if wordCount == 0 or wordLen == 0:
            return []
        
        # Keep the frequency of every word in a HashMap
        wordFreq = {}
        for w in words:
            if w not in wordFreq:
                wordFreq[w] = 0
            wordFreq[w] += 1
            

        indices = []
        # Starting from every index in the string, try to match all the words.
        # since we know wordLen, we know how many String chars are needed to be possible
        # example catfoxcat, ["cat", "fox"] the min window is 2 words * 3 wordLen  = 6 chars
        # 9 chars in S, window = 6 chars, so can only iterate 4 times
        # catfox, atfoxc, tfoxca, foxcat
        for i in range((len(s) - wordCount * wordLen) + 1):
            # In each iteration, keep track of all the words that we have already seen in another map.
            seen = {}
            for j in range(wordCount):
                nextWordIndex = i + j * wordLen
                word = s[nextWordIndex:nextWordIndex+wordLen]
                
                # word is not found, move to next char in the string.
                if word not in wordFreq:
                    break
                    
                if word not in seen:
                    seen[word] = 0
                seen[word] += 1
                
                # higher frequency than required, move to next char in string
                if seen[word] > wordFreq[word]:
                    break
                    
                # Store the start index if we have found all the words.
                if j + 1 == wordCount:
                    indices.append(i)
        return indices
            
def main():
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo","bar"])) # [0,9]
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good", "best", "word"])) # []
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo", "the"])) # [6,9,12]
main()