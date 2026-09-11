def greedy_matching(workers_pref, companies_pref, worker_wages, company_budgets):
    matches = {}
    for worker in workers_pref:
        for company in workers_pref[worker]:
            if company in matches:
                pass
            elif company_budgets[company] >= worker_wages[worker]:
                matches[company] = worker
                break 
    return matches