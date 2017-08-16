def schedule(jobs):
    jobs.sort(key= lambda x: x[1])
    q = []
    q.append(jobs[0])
    maxi = 0
    for i in xrange(1, len(jobs)):
        while(q and q[0][1] < jobs[i][0]):
            q.pop(0)

        q.insert(0, jobs[i])
        maxi = max(maxi, len(q))
    return maxi

arr  = [9.00,  9.40, 9.50,  11.00, 15.00, 18.00]
dep  = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
jobs = []
for i in xrange(len(arr)):
    jobs.append((arr[i], dep[i]))

print schedule(jobs)
