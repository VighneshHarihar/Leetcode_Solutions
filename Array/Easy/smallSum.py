import math


def smallSum(arr, k):
    winSum, winStart = 0, 0
    minSum = math.inf
    res = []

    for winEnd in range(len(arr)):
        winSum += arr[winEnd]

        while winSum >= k:
            res.append(arr[winStart:winEnd+1])
            minSum = min(minSum, winEnd-winStart+1)
            winSum -= arr[winStart]
            winStart += 1
    if minSum == math.inf:
        return 0
    return minSum


arr = [3, 4, 1, 1, 6]
k = 8
print(smallSum(arr, k))
