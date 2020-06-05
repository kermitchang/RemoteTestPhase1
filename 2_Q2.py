class Solution:
    def devideSum(self, src: int) -> int:
        #print(src)
        dstList = []
        start = 0
        while(start < src):
            start = start + 1
            if start % 15 == 0:
                dstList.append(start)
            elif start % 3 == 0:
                continue
            elif start % 5 == 0:
                continue
            else:
                dstList.append(start)
        print(dstList)
        return len(dstList)

def main():
    solution = Solution()
    data = 30
    print(solution.devideSum(data))

if __name__== "__main__":
    main()
