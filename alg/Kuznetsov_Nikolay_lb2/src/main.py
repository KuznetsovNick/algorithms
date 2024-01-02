from modules.scan_matrix import scan_matrix
from modules.merge import merge


def main():
    arr = scan_matrix()
    m_arr = merge(arr)
    final_output = []
    for i in m_arr:
        final_output.append(str(i.ind))
    print(' '.join(final_output))


if __name__ == "__main__":
    main()
