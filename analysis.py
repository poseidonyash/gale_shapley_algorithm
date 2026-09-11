from gale_shapley import gale_shapley
from data_generator import workers_preference, companies_preference
import copy
original_workers_pref = copy.deepcopy(workers_preference)
original_companies_pref = copy.deepcopy(companies_preference)
matches = gale_shapley(workers_preference, companies_preference)
worker_ranks = []
company_ranks = []
for company, worker in matches.items():
    company_rank = original_companies_pref[company].index(worker) + 1 # adding +1 to allow the rank to begin from 1 not 0
    worker_rank = original_workers_pref[worker].index(company) + 1
    
    company_ranks.append(worker_rank) # The company's satisfaction with their worker
    worker_ranks.append(company_rank)


avg_worker_rank = sum(worker_ranks)/len(worker_ranks)
avg_company_rank = sum(company_ranks)/len(company_ranks)

print(f"Average Worker Satisfaction: Got their #{avg_company_rank:.2f} choice")
print(f"Average Company Satisfaction: Got their #{avg_worker_rank:.2f} choice")