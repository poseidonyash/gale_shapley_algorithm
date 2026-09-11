from gale_shapley import gale_shapley
from greedy_matching import greedy_matching
from data_generator import generate_market_preferences
import copy

workers_pref, companies_pref, wages, budgets = generate_market_preferences(500, 500)

original_workers_pref = copy.deepcopy(workers_pref)
original_companies_pref = copy.deepcopy(companies_pref)

gs_matches = gale_shapley(copy.deepcopy(workers_pref), copy.deepcopy(companies_pref), wages, budgets)
greedy_matches = greedy_matching(copy.deepcopy(workers_pref), copy.deepcopy(companies_pref), wages, budgets)

def calculate_metrics(matches, name):
    worker_ranks = []
    company_ranks = []
    total_gmv = 0
    
    for company, worker in matches.items():
        company_ranks.append(original_companies_pref[company].index(worker) + 1)
        worker_ranks.append(original_workers_pref[worker].index(company) + 1)
        total_gmv += wages[worker]

    fill_rate = (len(matches) / len(original_workers_pref)) * 100

    print(f"--- {name} Results ---")
    print(f"Fill Rate: {fill_rate:.1f}%")
    print(f"Total GMV: ${total_gmv:,.2f}")
    print(f"Avg Worker Rank: {sum(worker_ranks)/len(worker_ranks):.2f}")
    print(f"Avg Company Rank: {sum(company_ranks)/len(company_ranks):.2f}\n")

calculate_metrics(greedy_matches, "Greedy (First-Come, First-Served)")
calculate_metrics(gs_matches, "Gale-Shapley")