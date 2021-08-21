from os import name, stat
import statistics

with open('ex36.txt', 'r') as data:
    times = data.readlines()
    for i in times:
        i.strip('\n')
    
    results = list(map(int, times))

def stats():
    stats_mean = statistics.mean(results)
    stats_max = max(results)
    stat_min = min(results)
    stats_stddev = statistics.stdev(results)

    print('Statistics from your file:\n')
    print(f'Data:\n{results}\n\nThe Minimum is: {stat_min}\nThe Maximum is: {stats_max}\nThe mean is: {stats_mean}\nThe Standard Deviations is: {stats_stddev}')

if __name__ == '__main__':
    stats()