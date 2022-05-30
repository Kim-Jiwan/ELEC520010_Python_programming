num_graph = {
    1 : [2, 3],
    2 : [1, 4, 5],
    3 : [1],
    4 : [2],
    5 : [2]
}

char_graph = {
    "A" : ["B", "C"],
    "B" : ["A", "D", "E"],
    "C" : ["A", "F", "G"],
    "D" : ["B", "H", "I"],
    "E" : ["B", "J"],
    "F" : ["C", "L"],
    "G" : ["C"],
    "H" : ["D"],
    "I" : ["D", "K"],
    "J" : ["E"],
    "K" : ["I"],
    "L" : ["F"]
}

# 너비 우선 탐색, BFS
def searching(graph, start):

    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)

        for num in graph[p]:
            if num not in done:
                qu.append(num)
                done.add(num)

searching(num_graph, 2)
print()
searching(char_graph, "A")