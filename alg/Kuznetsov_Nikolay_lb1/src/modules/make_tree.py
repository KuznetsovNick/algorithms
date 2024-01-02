def make_tree(parents):
    leafs = [i for i in range(0, len(parents))]
    for i in range(len(parents)):
        try:
            leafs.remove(parents[i])
        except:
            pass
    return leafs
