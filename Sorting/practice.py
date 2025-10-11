def merge_interval(intervals):
    merge_intervals=[]
    for interval in intervals:
        if len(merge_intervals)==0:
            merge_intervals.append(interval)
        else:
            if merge_intervals[-1][1] < interval[0]:
                merge_intervals.append(interval)
            else:
                merge_intervals[-1][1]=interval[1]

    return merge_intervals

print(merge_interval([[1,4],[1,5]]))