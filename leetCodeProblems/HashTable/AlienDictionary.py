"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_number = 0
        order_dict = dict()
        for elem in order:
            order_dict[elem] = order_number
            order_number += 1

        order_correct = True
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            order_number_1 = []
            order_number_2 = []
            for elem in word_1:
                order_number_1.append(order_dict[elem])

            for elem in word_2:
                order_number_2.append(order_dict[elem])

            for j in range(len(order_number_1)):
                if j < len(order_number_2):
                    if order_number_2[j] < order_number_1[j]:
                        order_correct = False
                        break
                    elif order_number_2[j] > order_number_1[j]:
                        break
                    else:
                        pass
                else:
                    order_correct = False
                    break

            if order_correct == False:
                return order_correct

        return order_correct