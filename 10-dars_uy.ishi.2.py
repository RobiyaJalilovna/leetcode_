class Solution:
    def sortPeople(self, names: list, heights: list):
        a = {}
        b = []
        for i in range(len(names)):
            a[heights[i]] = names[i]

        arr = list(a.keys())

        arr.sort(reverse=True)
        print(arr)
        for i in arr:
            b.append(a[i])
        return b
