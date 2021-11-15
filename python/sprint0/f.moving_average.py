def moving_average(timeseries, k):
    result = []
    for begin_index in range(0, len(timeseries) - k):
        end_index = begin_index + k
        current_sum = 0
        for v in timeseries[begin_index:end_index]:
            current_sum += v
            current_avg = current_sum / k
            result.append(current_avg)
    return result


def main():
    ts = list(map(int, input().split()))
    k = int(input())
    print(moving_average(ts, k))


if __name__ == '__main__':
    main()
