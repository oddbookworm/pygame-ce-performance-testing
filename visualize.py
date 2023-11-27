import json
from statistics import mean, stdev
from os.path import exists
from os import mkdir

import matplotlib.pyplot as plt

upstream_data = {}
ce_data = {}

def filter_outliers(data: list[float]) -> list[float]:
    data_mean = mean(data)
    data_sigma = stdev(data)
    
    filtered_data = [point for point in data if abs(point-data_mean) <= 2 * data_sigma]
    
    return filtered_data

if not exists("figures"):
    mkdir("figures")

for python_version in ["3.10.11", "3.11.5", "3.12.0"]:
    with open(f"raw_stats/({python_version})pygame-output.json", "r") as upstream:
        upstream_data = json.load(upstream)
        
    with open(f"raw_stats/({python_version})pygame-ce-output.json", "r") as ce:
        ce_data = json.load(ce)
    
    for size in ["Small", "Medium", "Large"]:
        for scale in ["Small", "Medium", "Large"]:
            upstream = filter_outliers(upstream_data[f"{size} Surface"][f"{scale} Multiplier"])
            ce = filter_outliers(ce_data[f"{size} Surface"][f"{scale} Multiplier"])

            fig = plt.figure()
            fig.set_size_inches((fig.get_size_inches()[0], fig.get_size_inches()[1]+1))
            plt.plot(range(len(upstream)), upstream)
            plt.plot(range(len(ce)), ce)
            plt.legend(["Upstream Pygame 2.5.2", "Pygame-ce 2.3.2"])
            plt.xlabel("Iteration")
            plt.ylabel("time taken (seconds)")
            title = f"Pygame vs Pygame-ce pygame.transform.scale\n{python_version = }\n"
            match size:
                case "Small":
                    title += "10x10 pixel source surface, "
                case "Medium":
                    title += "100x100 pixel source surface, "
                case "Large":
                    title += "1000x1000 pixel source surface, "
                    
            match scale:
                case "Small":
                    title += "2x scale"
                case "Medium":
                    title += "10x scale"
                case "Large":
                    title += "50x scale"
            
            plt.title(title)
            plt.savefig(f"figures/{size}-{scale}.png")
            plt.close()