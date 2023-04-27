def interval_scheduling(jobs):
    # sort jobs by finish time in non-decreasing order
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    # initialize empty subset of jobs
    S = []
    # loop through jobs
    for job in sorted_jobs:
        # if job doesn't overlap with any jobs in S, add it to S
        if not any(job[0] < end for (start, end) in S):
            S.append(job)
    return S

# example usage
jobs = [(0, 6), (1, 4), (3, 5), (5, 7), (7, 8), (8, 10), (10,15), (10,13), (13,16), (15,18), (16,18)]
subset = interval_scheduling(jobs)
print(subset)