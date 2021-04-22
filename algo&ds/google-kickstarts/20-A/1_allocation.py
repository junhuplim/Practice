def main():
    def allocate(store, houses):
        _, dollars, = store
        sorted_houses = sorted(houses)
        count = 0
        for house in sorted_houses:
            count += 1 if dollars >= house else 0
            dollars -= house if dollars >= house else 0

        return count

    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            store = input().split()
            houses = input().split()
            store = list(map(lambda x: int(x), store))
            houses = list(map(lambda x: int(x), houses))
            print(f'Case #{i + 1}: ', allocate(store, houses))

    read_input()

if __name__ == "__main__":
    main()