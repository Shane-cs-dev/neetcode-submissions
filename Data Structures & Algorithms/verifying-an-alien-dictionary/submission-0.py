class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Build a dict for the order of this alien map
        index_dict = {char : idx for idx, char in enumerate(order)}

        # Loop through the word in words array and check each character
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            for j in range(len(word1)):
                if j == len(word2): # If word1 is longer than word2 and no mismatch
                    return False
                if word1[j] != word2[j]: # Compare the order if the char is not same
                    if index_dict[word2[j]] < index_dict[word1[j]]:
                        return False
                    break # Prove that the string is sorted in alien order
        
        return True