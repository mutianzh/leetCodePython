"""
Given A and B two interval lists, A has no overlap inside A and B has no overlap inside B. Write the function to merge two interval lists, output the result with no overlap. Ask for a very efficient solution

A naive method can combine the two list, and sort and apply merge interval in the leetcode, but is not efficient enough.

For example,
A: [1,5], [10,14], [16,18]
B: [2,6], [8,10], [11,20]

output [1,6], [8, 20]
"""

def MergeTwoIntervalLists(A, B):
    i = 0
    j = 0
    result = []


    while i < len(A) and j < len(B):
        elem1 = A[i]
        elem2 = B[j]
        if elem1[0] < elem2[0]:
            picked = elem1
            i += 1
        elif elem1[0] > elem2[0]:
            picked = elem2
            j += 1

        if not result:
            result.append(picked)
        else:
            if result[-1][-1] < picked[0]:
                result.append(picked)
            else:
                result[-1] = [result[-1][0], max(picked[1], result[-1][1])]

    if i >= len(A) and j >= len(B):
        return result
    elif i >= len(A):
        picked = B[j]
        if result[-1][-1] < picked[0]:
            result.append(picked)
        else:
            result[-1] = [result[-1][0], max(picked[1], result[-1][1])]

        return result + B[j+1:]

    elif j >= len(B):
        picked = A[i]
        if result[-1][-1] < picked[0]:
            result.append(picked)
        else:
            result[-1] = [result[-1][0], max(picked[1], result[-1][1])]
        return result + A[i+1:]

A = [[1,5], [10,14], [16,18]]
B = [[2,6], [8,10], [11,20]]

print(MergeTwoIntervalLists(A, B))