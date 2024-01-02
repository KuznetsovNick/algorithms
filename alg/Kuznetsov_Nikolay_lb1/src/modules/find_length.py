def find_length(leafs, parents):
    mx_len = 0
    for i in range(len(leafs)):
        cur_len = 1
        cur_parent = parents[leafs[i]]
        while cur_parent != -1:
            cur_parent = parents[cur_parent]
            cur_len += 1
        if cur_len > mx_len:
            mx_len = cur_len
    return mx_len
