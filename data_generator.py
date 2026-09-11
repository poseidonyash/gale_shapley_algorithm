import numpy as np

def generate_market_preferences(n_workers=500, n_companies=500, noise_level=0.15):
    np.random.seed(42)
    
    worker_quality = np.random.normal(loc=0.5, scale=0.15, size=n_workers)
    company_prestige = np.random.normal(loc=0.5, scale=0.15, size=n_companies)
    
    worker_reserve_wages = 50000 + (worker_quality * 100000)
    company_max_budgets = 60000 + (company_prestige * 100000)
    
    company_noise = np.random.normal(loc=0, scale=noise_level, size=(n_companies, n_workers))
    worker_scores_for_companies = worker_quality + company_noise
    company_prefs = np.argsort(-worker_scores_for_companies, axis=1)
    
    worker_noise = np.random.normal(loc=0, scale=noise_level, size=(n_workers, n_companies))
    company_scores_for_workers = company_prestige + worker_noise
    worker_prefs = np.argsort(-company_scores_for_workers, axis=1)
    
    workers_dict, wages_dict = {}, {}
    for i in range(n_workers):
        workers_dict[f"worker {i}"] = [f"company {j}" for j in worker_prefs[i]]
        wages_dict[f"worker {i}"] = worker_reserve_wages[i]
        
    companies_dict, budgets_dict = {}, {}
    for i in range(n_companies):
        companies_dict[f"company {i}"] = [f"worker {j}" for j in company_prefs[i]]
        budgets_dict[f"company {i}"] = company_max_budgets[i]
    
    return workers_dict, companies_dict, wages_dict, budgets_dict