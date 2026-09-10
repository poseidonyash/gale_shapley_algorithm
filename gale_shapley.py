import numpy as np 

workers_preference = {
    "worker A": ["Google", "Microsoft", "Apple"], 
    "worker B": ["Google", "Microsoft", "Apple"],  
    "worker C": ["Apple", "Google", "Microsoft"]
}

companies_preference = {
    "Google": ["worker A", "worker B", "worker C"], 
    "Microsoft": ["worker B", "worker A", "worker C"], 
    "Apple": ["worker C", "worker B", "worker A"]
}

matches = {}
workers = list(workers_preference.keys())

while workers:
    worker = workers.pop(0)
    #print(worker)
    top_choice = workers_preference[worker].pop(0)
    #print(top_choice)
    if top_choice in matches:
        current_worker = matches[top_choice]
        worker_rank = companies_preference[top_choice].index(worker)
        current_worker_rank = companies_preference[top_choice].index(current_worker)
        if worker_rank < current_worker_rank:
            matches[top_choice] = worker
            workers.append(current_worker)
        else:
            workers.append(worker)
    else:
            matches[top_choice] = worker

print(matches)