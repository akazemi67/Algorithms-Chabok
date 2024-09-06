# Problem's Link: https://quera.org/problemset/9744

best_cost = 10**10
best_perm = []
job_costs = []

def check_jobs(eid, jobs, cost, n):
    global best_cost, best_perm
    if cost > best_cost:
        return

    if len(jobs)==n:
        if cost < best_cost:
            best_cost = cost
            best_perm = jobs[::]
            return 

    for j in range(n):
        e = eid + 1
        if not j in jobs:
            jobs.append(j)
            check_jobs(e, jobs, cost + job_costs[e][j], n)
            jobs.pop()


n = int(input())
for _ in range(n):
    row = list(map(int, input().split()))
    job_costs.append(row)

check_jobs(-1, [], 0, n)
for j in best_perm:
    print(j)

