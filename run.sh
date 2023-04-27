#!/bin/bash

traces="cc-14.trace.gz bfs-14.trace.gz"

repl_policies="fifo"

for repl_polc in $repl_policies
do 
    ./build_champsim.sh bimodal no no no no ${repl_polc} 1
    for trace in $traces
    do 
        echo ${repl_polc}
        echo ${trace}
        time ./run_champsim.sh bimodal-no-no-no-no-${repl_polc}-1core 20 30 ${trace}
    done
done

