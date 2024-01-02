from modules.process import process


def main():
    proc_kol, time_kol = map(int, input().split())
    times = list(map(int, input().split()))
    answer = process(proc_kol, time_kol, times)

    for i in answer:
        print(*i)


if __name__ == '__main__':
    main()
