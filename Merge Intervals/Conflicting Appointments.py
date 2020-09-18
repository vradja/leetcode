def can_attend_all_appointments(intervals):
    non_overlapping_intervals = list()
    for interval in sorted(intervals, key=lambda x: x[0]):
        if non_overlapping_intervals and interval[0] < non_overlapping_intervals[-1][1]:
            return False
        else:
            non_overlapping_intervals.append(interval)
    return True


def main():
    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
