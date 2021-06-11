import math
def main():
    def good_pairs(N, H):
        noEven = 0
        ans = 0
        for i in range(N):
            if H[i] % 2 == 0:
                noEven += 1
            else:
                for j in range(i + 1, N):
                    if H[j] % 2 == 0:
                        continue
                    if math.gcd(H[i], H[j]) > 1:
                        ans += 1

        for k in range(noEven):
            ans += N - noEven + k

        return ans

    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            N = int(input())
            H = input().split()
            H = list(map(lambda x: int(x), H))
            print(good_pairs(N, H))

    read_input()

if __name__ == "__main__":
    main()