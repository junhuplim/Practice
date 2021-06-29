def main():
    def solve(arr):
        ans = 0
        l, r = arr
        while l > 0 or r > 0:
            ans += r - l
            r = r // 10
            l = l // 10

        return ans

    number_tests = int(input())
    for _ in range(number_tests):
        arr = list(map(int, input().split()))
        print(solve(arr))

if __name__ == "__main__":
    main()