from modules.solve import solve


def main():
    pattern = input()
    text = input()
    answer = solve(pattern, text)
    print(*answer)


if __name__ == "__main__":
    main()
