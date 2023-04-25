def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for start_time, end_time in permanence_period:
            if start_time <= target_time <= end_time:
                count += 1
        return count
    except TypeError:
        return None
