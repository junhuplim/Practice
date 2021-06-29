import math
def main():
    def solve(N, L, R, H):
        H.sort()
        return helper(H, R) - helper(H, L - 1)

    def helper(H, lim):
        i, j = 0, len(H) - 1
        count = 0
        while i < j:
            if H[i] + H[j] <= lim:
                count += j - i
                i += 1
            else:
                j -= 1

        return count

    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            # N = int(input())
            N, L, R = input().split()
            # H = input()
            H = input().split()
            H = list(map(lambda x: int(x), H))
            print(solve(int(N), int(L), int(R), H))

    read_input()

if __name__ == "__main__":
    main()