#!/bin/bash
v=("erdos_renyi_1.py" "Barabasi-Albert_sample_2.py" "configuration_model_3.py" "geometric_configuration_4.py" "forest_fire_5.py" "stochastic_block_model_6.py")
cpp_file="kaidi"   

num_nodes="1000"
num_edges="5000"
python ${v[3]} $num_nodes $num_edges_per_node 0.25 > input.txt
g++ -std=c++11 ${cpp_file}.cpp -o ${cpp_file}
./${cpp_file} > ${v[3]}_${num_nodes}_${num_edges_per_node}.txt

