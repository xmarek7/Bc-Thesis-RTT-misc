from sys import argv
import pandas as pd

HELP = """Usage help: 
    First and second arguments are paths to text files with p-values
    Optional third arguments is number of required bins, defaults to 100
        """

def to_bins(first, second, bins) -> tuple[list[int]:, list[int]]:
    pd_first = pd.read_csv(first, header = None)
    pd_second = pd.read_csv(second, header=None)
    
    interval_size = 1 / bins
    bins_first = []
    bins_second = []

    bin_i = 0
    while bin_i < bins - 1:
        low = bin_i * interval_size
        up = (bin_i + 1) * interval_size

        bins_first.append(len(pd_first[(pd_first[0] < up) & (pd_first[0] >= low)]))
        bins_second.append(len(pd_second[(pd_second[0] < up) & (pd_second[0] >= low)]))

        bin_i += 1
        
    low = bin_i * interval_size
    up = (bin_i + 1) * interval_size

    bins_first.append(len(pd_first[(pd_first[0] <= up) & (pd_first[0] >= low)]))
    bins_second.append(len(pd_second[(pd_second[0] <= up) & (pd_second[0] >= low)]))

    return bins_first, bins_second


def check_bins(first: list[int], second: list[int], bins: int) -> tuple[list[float], list[float]]:
    first_size = sum(first)
    second_size = sum(second)


    diffs = []

    max_diff, max_bin = None, None

    for i in range(bins):
        fst_ratio = first[i] / first_size
        snd_ratio = second[i] / second_size

        if (fst_ratio == 0 and snd_ratio == 0):
            dif = 0

        else:
            mean_ratio = (fst_ratio + snd_ratio) / 2
            dif = abs(((fst_ratio - mean_ratio) / mean_ratio) * 100)

        diffs.append(dif)
        if max_diff is None or dif > max_diff:
            max_diff, max_bin = dif, i

    interval_size = 1 / bins
    print("Max difference from mean: {} in bin from {} to {}".format(max_diff, max_bin * interval_size, (max_bin + 1) * interval_size))
    #print(diffs)
    return diffs


def main():
    if len(argv) < 3 or len(argv) > 4 :
        print(HELP)
        return
    
    first = argv[1]
    second = argv[2]
    bins = 100
    if len(argv) == 4:
        bins = int(argv[3])
    
    f_bins, s_bins = to_bins(first, second, bins)
    difs = check_bins(f_bins, s_bins, bins)


if __name__ == "__main__":
    main()
