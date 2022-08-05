class Solution:
    def find_word_concatenation(self, s, words):
        result_indices = []
        if len(words) == 0 or len(words[0]) == 0:
            return []
        
        wordFreq = {}
        for w in words:
            if w not in wordFreq:
                wordFreq[w] = 0
            wordFreq[w] += 1
        print(s)
        print(wordFreq)

        wordLen = len(words[0])
        numWords = len(words)
        result_indices = []
        start = 0
        matches = 0
        numIterations = (len(s) - numWords * wordLen) + 1
        print("Iterations:", numIterations)
        for i in range(numIterations):
            seen = {}
            for j in range(0, numWords):
                nextWordIndex = i + j * wordLen
                word = s[nextWordIndex: nextWordIndex+wordLen]
                print(i, j, nextWordIndex, word)
                if word not in wordFreq:
                    break

                if word not in seen:
                    seen[word] = 0
                seen[word] += 1

                if seen[word] > wordFreq[word]:
                    break

                if j + 1 == numWords:
                    result_indices.append(i)
            

        return result_indices
def main():
    s = Solution()
    print(s.find_word_concatenation("catfoxcat", ["cat", "fox"]))
    # print(s.find_word_concatenation("catcatfoxfox", ["cat","fox"]))
    # print(s.find_word_concatenation("wordgoodgoodgoodbestword", ["word","good", "good", "good", "best"]))
    
main()