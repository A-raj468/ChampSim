import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#plotting, we generate two different plots for ipc and LLC miss rate
N = 4
ind = np.arange(N) 
width = 0.2

# exclusive data
#data--ipc  for each replacement policy we need data for different sizes
fifo_ipc= [0.17799, 0.15935, 0.129338, 0.0976919]
fifo_dram_access= [4.893877863426232, 4.762422327043794, 4.689423963257668, 4.196826549038916]
lfu_ipc= [0.183332, 0.162209, 0.130495, 0.0959638]
lfu_dram_access= [4.706307599829874, 4.647960053087353, 4.621118906416056, 4.34823900692747]
lru_ipc= [0.181809, 0.161778, 0.130384, 0.094788]
lru_dram_access= [4.7594008436466435, 4.6680290864205, 4.638396303700061, 4.4691096267530135]
random_ipc= [0.178359, 0.159699, 0.13207, 0.106648]
random_dram_access= [4.893276778838946, 4.75341583025707, 4.494922457984556, 3.4324649682820305]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(1,2,1)
bar1 = plt.bar(ind, lfu_ipc, width, color = 'r')
bar2 = plt.bar(ind+width, fifo_ipc, width, color='g')
bar3 = plt.bar(ind+width*2, lru_ipc, width, color = 'b')
bar4 = plt.bar(ind+width*3, random_ipc, width, color = 'c')
# bar4 = plt.bar(ind+width*3, lruipc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("IPC comparison for Inclusive cache hierarchy", fontsize=10)

plt.subplot(1,2,2)
bar1 = plt.bar(ind, lfu_dram_access, width, color = 'r')
bar2 = plt.bar(ind+width, fifo_dram_access, width, color='g')
bar3 = plt.bar(ind+width*2, lru_dram_access, width, color = 'b')
bar4 = plt.bar(ind+width*3, random_dram_access, width, color = 'c')
# bar8 = plt.bar(ind+width*3, lruLLCmissrate, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("DRAM Access(%)")
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM ACCESS RATE comparison for Inclusive cache hierarchy", fontsize=10)

plt.show()

