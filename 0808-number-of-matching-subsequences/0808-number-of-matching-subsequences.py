from collections import defaultdict

class Solution:
    
    def numMatchingSubseq(self, S, words):

        word_dict = defaultdict(list)
        count = 0

        for w in words:
            word_dict[w[0]].append(w)



        for char in S:
 
            words_start_char = word_dict[char]

            word_dict[char] = []

            for word in words_start_char:
                if len(word) ==1:
                    count+=1
                else:
                    word_dict[word[1]].append(word[1:])

        return count


        