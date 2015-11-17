#!/bin/bash
v=("erdos_renyi_1.py" "Barabasi-Albert_sample_2.py" "configuration_model_3.py" "geometric_configuration_4.py" "forest_fire_5.py" "stochastic_block_model_6.py")
for num_nodes in $(seq 100 100 1000)
do
  for num_edges in $(seq 1000 5000 1000)
  do 
    python ${v[1]} $num_nodes $num_edges > input.txt 
    g++ -std=c++11 kaidi.cpp -o kaidi
    ./kaidi > output${num_nodes}_${num_edges}.txt
  done
done
