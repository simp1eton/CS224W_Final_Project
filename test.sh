#!/bin/bash
v=("erdos_renyi_1.py" "Barabasi-Albert_sample_2.py" "configuration_model_3.py" "geometric_configuration_4.py" "forest_fire_5.py" "stochastic_block_model_6.py")
for num_nodes in $(seq 100 100 1000)
do
  for num_edges in $(seq 1000 5000 1000)
  do 
    python ${v[0]} $num_nodes $num_edges > input.txt 
    g++ -std=c++11 kaidi.cpp -o kaidi
    ./kaidi > ${v[0]}_${num_nodes}_${num_edges}.txt
  done
done


for num_nodes in $(seq 100 100 1000)
do
  for num_edges_per_node in $(seq 2 20 2)
  do
    python ${v[1]} $num_nodes $num_edges_per_node > input.txt
    g++ -std=c++11 kaidi.cpp -o kaidi
    ./kaidi > ${v[1]}_${num_nodes}_${num_edges_per_node}.txt
  done
done


for num_nodes in $(seq 100 100 1000)
do
  for num_edges in $(seq 1000 5000 1000)
  do
    python ${v[2]} $num_nodes $num_edges > input.txt
    g++ -std=c++11 kaidi.cpp -o kaidi
    ./kaidi > ${v[2]}_${num_nodes}_${num_edges}.txt
  done
done

for num_nodes in $(seq 100 100 1000)
do
  for num_edges_per_node in $(seq 1000 5000 1000)
  do
    python ${v[3]} $num_nodes $num_edges_per_node 0.25 > input.txt
    g++ -std=c++11 kaidi.cpp -o kaidi
    ./kaidi > ${v[3]}_${num_nodes}_${num_edges_per_node}.txt
  done
done


for num_nodes in $(seq 100 100 1000)
do
  python ${v[4]} $num_nodes 0.5 0.5 > input.txt
  g++ -std=c++11 kaidi.cpp -o kaidi
  ./kaidi > ${v[4]}_${num_nodes}.txt
done

for num_nodes in $(seq 100 100 1000)
do
  python ${v[5]} 4 0.8 0.3 > input.txt
  g++ -std=c++11 kaidi.cpp -o kaidi
  ./kaidi > ${v[5]}_${num_nodes}.txt
done
