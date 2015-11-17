#!/bin/bash
v=("erdos_renyi_1.py" "Barabasi-Albert_sample_2.py" "configuration_model_3.py" "geometric_configuration_4.py" "forest_fire_5.py" "stochastic_block_model_6.py")
cpp_file="kaidi"   

num_nodes="1000"
num_edges="5000" 
python ${v[0]} $num_nodes $num_edges > input.txt 
g++ -std=c++11 ${cpp_file}.cpp -o ${cpp_file}
./${cpp_file} > ${v[0]}_${num_nodes}_${num_edges}.txt

num_nodes="1000"
num_edges_per_node="2"
python ${v[1]} $num_nodes $num_edges_per_node > input.txt
g++ -std=c++11 ${cpp_file}.cpp -o ${cpp_file}
./${cpp_file} > ${v[1]}_${num_nodes}_${num_edges_per_node}.txt


num_nodes="1000"
num_edges="5000"
python ${v[2]} $num_nodes $num_edges > input.txt
g++ -std=c++11 ${cpp_file}.cpp -o ${cpp_file}
./${cpp_file} > ${v[2]}_${num_nodes}_${num_edges}.txt

num_nodes="1000"
num_edges="5000"
python ${v[3]} $num_nodes $num_edges_per_node 0.25 > input.txt
g++ -std=c++11 ${cpp_file}.cpp -o ${cpp_file}
./${cpp_file} > ${v[3]}_${num_nodes}_${num_edges_per_node}.txt

num_nodes="1000"
python ${v[4]} $num_nodes 0.5 0.5 > input.txt
g++ -std=c++11 ${cpp_file}.cpp -o ${cpp_file}
./${cpp_file} > ${v[4]}_${num_nodes}.txt

num_nodes="1000"
python ${v[5]} 4 0.8 0.3 > input.txt
g++ -std=c++11 ${cpp_file}.cpp -o ${cpp_file}
./${cpp_file} > ${v[5]}_${num_nodes}.txt
