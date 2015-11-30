from util import read_file
import random

def generate_set(adj_list, threshold, start):
    queue = [(start, 0)]
    visited = set()
    visited.add(start)

    while len(queue) > 0:
        front = queue.pop(0)
        if front[1] > threshold:
            return visited

        for adj in adj_list[front[0]]:
            if adj in visited: continue
            visited.add(adj)
            queue.append((adj, front[1] + 1))
    return visited


if __name__ == "__main__":
    random.seed()
    graph = read_file("input.txt")
    graph.preprocess()
    adj_list = graph.G

    num_sets = 500
    threshold = 1
    budget = 10

    possible_nodes = set()
    start_nodes = random.sample(range(graph.N), num_sets)
    sets = []
    for start in start_nodes:
        rr_set = generate_set(adj_list, threshold, start)

        possible_nodes = possible_nodes.union(rr_set)
        sets.append(rr_set)

    results = []
    for _ in range(budget):
        max_cover_node = None
        max_cover_count = 0

        for node in possible_nodes:
            count = 0
            for rr_set in sets:
                if node in rr_set: count += 1
            if count > max_cover_count:
                max_cover_count = count
                max_cover_node = node

        if max_cover_node != None:
            for rr_set in sets:
                if max_cover_node in rr_set:
                    sets.remove(rr_set)
            possible_nodes.remove(max_cover_node)
            results.append(max_cover_node)

    print results
    print graph.avg_dist(results)





