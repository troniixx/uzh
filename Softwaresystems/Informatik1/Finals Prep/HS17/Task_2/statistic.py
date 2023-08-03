def compute_stats(lst):
    # find second highest nr, average and median
    # if len(lst) odd median middle value else average of the two central numbers
    sorted_list = sorted(lst)
    stats = []
    if lst == []:
        return []
    else:
        #second largest
        second = sorted_list[-2]
        stats.append(second)

        #average
        sums = 0
        for i in lst:
            sums += i
        avg = sums / len(lst)
        stats.append(avg)

        #median
        len_list = len(lst)
        index = (len_list - 1) // 2
        if (len_list % 2):
            stats.append(sorted_list[index])
        else:
            stats.append((sorted_list[index] + sorted_list[index + 1])/2.0)

    return stats

stats = compute_stats([])
stats1 = compute_stats([1,12,4,5,8])
print(stats)
print(stats1)

