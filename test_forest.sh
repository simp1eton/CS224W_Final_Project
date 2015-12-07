#!/bin/bash
v=("erdos_renyi_1.py" "Barabasi-Albert_sample_2.py" "configuration_model_3.py" "geometric_configuration_4.py" "forest_fire_5.py" "stochastic_block_model_6.py")
cpp_file="kaidi"   

num_nodes="1000"
python ${v[4]} $num_nodes 0.5 0.5 > input.txt
g++ -std=c++11 ${cpp_file}.cpp -o ${cpp_file}
./${cpp_file} > ${v[4]}_${num_nodes}.txt

