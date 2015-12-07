#/bin/bash
v=("erdos_renyi_1.py" "Barabasi-Albert_sample_2.py" "configuration_model_3.py" "geometric_configuration_4.py" "forest_fire_5.py" "stochastic_block_model_6.py")
for i in `seq 1 50`;
do 
  python ${v[0]} > input1-${i}.txt 
done
for i in `seq 1 50`;
do 
  python ${v[2]} > input3-${i}.txt 
done
