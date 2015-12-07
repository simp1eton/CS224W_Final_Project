#/bin/bash
v=("erdos_renyi_1.py" "Barabasi-Albert_sample_2.py" "configuration_model_3.py" "geometric_configuration_4.py" "forest_fire_5.py" "stochastic_block_model_6.py")
for i in `seq 1 50`;
do 
  python ${v[4]} > input5-${i}-${v[4]}.txt 
done
for i in `seq 1 50`;
do 
  python ${v[5]} > input6-${i}-${v[5]}.txt 
done
