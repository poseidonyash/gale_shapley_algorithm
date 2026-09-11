def gale_shapley(workers_pref, companies_pref, worker_wages, company_budgets):
    matches = {}
    workers = list(workers_pref.keys())
    while workers:
        worker = workers.pop(0)
        if not workers_pref[worker]:
            continue
        top_choice = workers_pref[worker].pop(0)
        if company_budgets[top_choice] < worker_wages[worker]:
            workers.append(worker)
            continue
        if top_choice not in matches:
            matches[top_choice] = worker
        else:
            current_worker = matches[top_choice]
            worker_rank = companies_pref[top_choice].index(worker)
            current_worker_rank = companies_pref[top_choice].index(current_worker)
            if worker_rank < current_worker_rank:
                matches[top_choice] = worker
                workers.append(current_worker)
            else:
                workers.append(worker)
    return matches