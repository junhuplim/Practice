def main():
    def k_beautiful_strings(N, K, H):
        if N % K != 0:
            return - 1



    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            N, K = input().split()
            H = input().split()
            H = list(map(lambda x: int(x), H))
            print(k_beautiful_strings(int(N), int(K), H))

    read_input()

if __name__ == "__main__":
    main()