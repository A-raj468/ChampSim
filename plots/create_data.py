import re

traces = ['bfs-14.trace.gz', 'cc-14.trace.gz']
heirarcies = ['INCLUSIVE', 'non-inclusive', 'semi-exclusive', 'exclusive']
# heirarcies = ['exclusive']
repls = ['fifo', 'lfu', 'lru', 'random']
sizes = [1, 2, 4, 8]

plot_data = {}

for trace in traces:
    # print(f"TRACE: {trace}")
    plot_data[trace] = {}
    for heirarcy in heirarcies:
        # print(f"HEIRARCY: {heirarcy}")
        plot_data[trace][heirarcy] = {}
        for repl in repls:
            # print(f"REPLACEMENT POLICY: {repl}")
            plot_data[trace][heirarcy][repl] = {}
            plot_data[trace][heirarcy][repl]["ipc"] = []
            plot_data[trace][heirarcy][repl]["dram_access"] = []
            for size in sizes:
                # print(f"SIZE: {size}")
                with open(f'../results_30M/{trace}-bimodal-no-no-no-no-{repl}-1core-{heirarcy}-{size}.txt', mode='r') as f:
                    data = f.read()
                    
                    reipc = r"\bCPU 0\s+cumulative\s+IPC:\s*(\d+(?:\.\d+)?)\b"
                    rel1i = r"\bL1I\s+TOTAL\s+ACCESS:\s*(\d+(?:\.\d+)?)\b"
                    rel1d = r"\bL1D\s+TOTAL\s+ACCESS:\s*(\d+(?:\.\d+)?)\b"
                    rellc = r"\bLLC\s+TOTAL\s+ACCESS:\s*\d+(?:\.\d+)?\s+HIT:\s+\d+(?:\.\d+)?\s+MISS:\s+(\d+(?:\.\d+)?)\b"

                    cummulative_ipc = float(re.search(reipc, data).group(1))
                    total_access = float(re.search(rel1i, data).group(1)) + float(re.search(rel1d, data).group(1))
                    llc_miss = float(re.search(rellc, data).group(1))
                    # print(cummulative_ipc, total_access, llc_miss, total_access/llc_miss)
                    plot_data[trace][heirarcy][repl]["ipc"].append(cummulative_ipc)
                    plot_data[trace][heirarcy][repl]["dram_access"].append(llc_miss/total_access*100)

# print()
# print(plot_data)
s = ''
for trace, stats1 in plot_data.items():
    print(s, end='')
    print(trace)
    # print(stats1)
    t = s + '\t'
    for heir, stats2 in stats1.items():
        print(t, end='')
        print(heir)
        # print(stats2)
        u = t + '\t'
        for policy, stats3 in stats2.items():
            # print(u, end='')
            # print(policy)
            # print(stats3)
            # v = u + '\t'
            for metric, stats4 in stats3.items():
                print(u, end='')
                print(f"{policy}_{metric}= {stats4}")