from util import read_file
import random
import time
import numpy
import sys

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
    num_sets = 500
    threshold = 1
    budget = 20
    graph_type = int(sys.argv[1])

    stats = [[] for _ in range(budget)]
    ans = [[] for _ in range(budget)]

    for i in range(1, 51):
        random.seed()
        filename = "../DATA/mass_data/input" + `graph_type` + "-" + `i` + ".txt"
        graph = read_file(filename)
        adj_list = graph.G

        start_time = time.time()
        possible_nodes = set()
        start_nodes = random.sample(range(graph.N), num_sets)
        sets = []
        for start in start_nodes:
            rr_set = generate_set(adj_list, threshold, start)

            possible_nodes = possible_nodes.union(rr_set)
            sets.append(rr_set)
        results = []
        end_time = time.time()
        total_time = end_time - start_time

        for curr_budget in range(budget):
            start_time = time.time()
            max_cover_node = None
            max_cover_count = 0

            for node in possible_nodes:
                count = 0
                for rr_set in sets:
                    if node in rr_set: count += 1
                if count >= max_cover_count:
                    max_cover_count = count
                    max_cover_node = node

            if max_cover_node != None:
                for rr_set in sets:
                    if max_cover_node in rr_set:
                        sets.remove(rr_set)
                possible_nodes.remove(max_cover_node)
                results.append(max_cover_node)
            end_time = time.time()
            total_time += end_time - start_time
            avg_dist = graph.avg_dist(results)

            #print results
            #print total_time, avg_dist

            stats[curr_budget].append(total_time)
            ans[curr_budget].append(avg_dist)

    #print '=' * 50
    for i in range(budget):
        stats_list = stats[i]
        ans_list = ans[i]
        stats_std = numpy.std(stats_list)
        stats_mean = numpy.mean(stats_list)
        ans_std = numpy.std(ans_list)
        ans_mean = numpy.mean(ans_list)
        print stats_mean, stats_std, ans_mean, ans_std
