from util import read_file
import random
import time
import numpy
import sys

if __name__ == "__main__":
    budget = 20
    graph_type = int(sys.argv[1])

    stats = [[] for _ in range(budget)]
    ans = [[] for _ in range(budget)]

    for i in range(1, 51):
        random.seed()
        filename = "../DATA/mass_data/input" + `graph_type` + "-" + `i` + ".txt"
        graph = read_file(filename)

        for curr_budget in range(budget):
            start_time = time.time()
            seeds = random.sample(range(graph.N), curr_budget + 1)
            end_time = time.time()
            total_time = end_time - start_time
            avg_dist = graph.avg_dist(seeds)

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





