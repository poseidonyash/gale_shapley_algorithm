from gale_shapley import gale_shapley
from greedy_matching import greedy_matching
from data_generator import generate_market_preferences
import copy
import matplotlib.pyplot as plt
import seaborn as sns

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

    return company_ranks,worker_ranks

greedy_worker_ranks, greedy_company_ranks = calculate_metrics(greedy_matches, "Greedy (First-Come, First-Served)")
gale_shapley_worker_ranks, gale_shapley_company_ranks = calculate_metrics(gs_matches, "Gale-Shapley")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Marketplace Rank Distributions: Greedy vs. Deferred Acceptance", fontsize=18, fontweight='bold')

sns.histplot(greedy_worker_ranks, bins=40, ax=axes[0, 0], color="tomato", kde=True)
axes[0, 0].set_title("Greedy: Worker Rank Distribution", fontweight='bold')
axes[0, 0].set_ylabel("Number of Matches")

sns.histplot(greedy_company_ranks, bins=40, ax=axes[0, 1], color="darkred", kde=True)
axes[0, 1].set_title("Greedy: Company Rank Distribution", fontweight='bold')
axes[0, 1].set_ylabel("")

# Gale-Shapley Plots (Bottom Row)
sns.histplot(gale_shapley_worker_ranks, bins=40, ax=axes[1, 0], color="dodgerblue", kde=True)
axes[1, 0].set_title("Gale-Shapley: Worker Rank Distribution", fontweight='bold')
axes[1, 0].set_xlabel("Preference Rank (1 = Top Choice)")
axes[1, 0].set_ylabel("Number of Matches")

sns.histplot(gale_shapley_company_ranks, bins=40, ax=axes[1, 1], color="navy", kde=True)
axes[1, 1].set_title("Gale-Shapley: Company Rank Distribution", fontweight='bold')
axes[1, 1].set_xlabel("Preference Rank (1 = Top Choice)")
axes[1, 1].set_ylabel("")

plt.savefig("greedy vs gale-shapley distribution.png")
plt.show()