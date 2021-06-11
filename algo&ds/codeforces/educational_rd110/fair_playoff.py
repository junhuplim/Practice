def main():
    def fair(H):
        check = min(H[2], H[3]) > max(H[0], H[1]) or min(H[0], H[1]) > max(H[2], H[3])
        return 'NO' if check else 'YES'

    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            H = input().split()
            H = list(map(lambda x: int(x), H))
            print(fair(H))

    read_input()

if __name__ == "__main__":
    main()