from gale_shapley import gale_shapley
from greedy_matching import greedy_matching
from data_generator import workers_preference, companies_preference
import copy

original_workers_pref = copy.deepcopy(workers_preference)
original_companies_pref = copy.deepcopy(companies_preference)

gale_shapley_matches = gale_shapley(copy.deepcopy(workers_preference), copy.deepcopy(companies_preference))
greedy_matches = greedy_matching(copy.deepcopy(workers_preference), copy.deepcopy(companies_preference))

def calculate_averages(matches, name):
    worker_ranks = []
    company_ranks = []
    
    for company, worker in matches.items():
        company_ranks.append(original_companies_pref[company].index(worker) + 1)
        worker_ranks.append(original_workers_pref[worker].index(company) + 1)

    print(f"--- {name} Results ---")
    print(f"Avg Worker Rank: {sum(worker_ranks)/len(worker_ranks):.2f}")
    print(f"Avg Company Rank: {sum(company_ranks)/len(company_ranks):.2f}\n")

calculate_averages(greedy_matches, "Greedy (First-Come, First-Served)")
calculate_averages(gale_shapley_matches, "Gale-Shapley")