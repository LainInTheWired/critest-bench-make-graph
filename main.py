import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os


# path = 'result/containerd_2024-01-14_02-43-03/benchmark_crun_2024-01-14_02-43-03.txt'
path = 'result/%s/benchmark_%s_2024-01-14_02-43-03.txt'
dirs = os.listdir('result/')

search_words = "create PodSandbox and container [duration]"

def extraction_result(dir,runtime):
    results = []
    p = path % (dir, runtime)
    with open(p) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if search_words in line:
            # print("line:" + line)
            results.append(line.split("|"))

    return results    

def avg(results):
    # results = extraction_result()
    total = 0
    for result in results:
        result = result[3].strip()
        print(result[:-2])
        if result[-2] != "m":
            print("result:" + result)
            total += float(result.strip()[:-1]) * 1000
        else:
            total += float(result.strip()[:-2])
    avgs = 0
    print(total)
    avgs = total/len(results)
    print(avgs)
    return avgs
# r = extraction_result()
# print(float(r[0][3].strip()[:-1]))
# print(r[1],sep="\n")
runtimes = ["runc","runsc","kata","crun"]
print(dirs)
for dir in dirs:
    avgs = []
    for runtime in runtimes:
        r = extraction_result(dir,runtime)
        avgs.append(avg(r))
    left = np.array([1, 2, 3, 4])
    print("avgs")
    print(avgs)
    height = np.array(avgs)
    plt.bar(left, height, tick_label=runtimes, align="center")
    # plt.bar(left, height)
    plt.title("" + dir + "start benchmark")
    plt.ylabel("ms")
    # plt.grid(True)

    plt.savefig("graph_img/" +dir + ".png", format="png", dpi=1000)


