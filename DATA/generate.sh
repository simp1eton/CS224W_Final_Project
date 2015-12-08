#/bin/bash
v=("erdos_renyi_1.py" "Barabasi-Albert_sample_2.py" "configuration_model_3.py" "geometric_configuration_4.py" "forest_fire_5.py" "stochastic_block_model_6.py")
for i in `seq 1 50`;
do 
  python ${v[4]} | sed 1,4d > input5-${i}.txt 
done


