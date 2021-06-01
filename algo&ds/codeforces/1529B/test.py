def main():
    def strange_sub(N, H):
        sorted_list = sorted(H)
        remove_count = 0
        max_idx = N - 1
        i, j = N - 2, N - 1
        while i >= 0:
            if abs(sorted_list[i] - sorted_list[j]) < sorted_list[max_idx]:
                remove_count += 1
                max_idx -= 1
            i -= 1
            j -= 1

        return N - remove_count


    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            N = int(input())
            H = input().split()
            H = list(map(lambda x: int(x), H))
            print(strange_sub(N, H))

    read_input()

if __name__ == "__main__":
    main()