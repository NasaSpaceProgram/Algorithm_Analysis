

n = int(input("How many jobs would you like to schedule?"))
jobs = []

for i in range(n):
    jobs.append(int(input("Please enter the time for job "+ str((i+1))+ ":")))

print(jobs)




#define this function
def schedule_it(jobs_list):
    #...
    return jobs_list



print(schedule_it(jobs))