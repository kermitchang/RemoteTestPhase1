
class Solution:
    def inverseString(self, src: str) -> str:
        #print(src)
        dst = ""
        data = src.split(" ")
        for subData in data:
            dst = dst + subData[::-1] + " "
        return dst[0:-1]

def main():
    solution = Solution()
    data = "Hello World"
    print(solution.inverseString(data))

if __name__== "__main__":
    main()
