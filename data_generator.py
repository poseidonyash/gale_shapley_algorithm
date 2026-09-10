import numpy as np 


def generate_market_preferences(n_workers=500, n_companys=500, noise_level=0.15):
    np.random.seed(42) # For reproducible simulation results
    
    # 1. Hidden Variables (The true underlying value of each agent)
    # Workers have a 'quality' score (e.g., skill level, efficiency)
    worker_quality = np.random.normal(loc=0.5, scale=0.15, size=n_workers)
    
    # companys have a 'prestige' score (e.g., brand value, budget size)
    company_prestige = np.random.normal(loc=0.5, scale=0.15, size=n_companys)
    
    # 2. companys ranking Workers
    # Base preference is worker_quality, but each company has subjective "noise"
    company_noise = np.random.normal(loc=0, scale=noise_level, size=(n_companys, n_workers))
    worker_scores_for_companys = worker_quality + company_noise
    
    # np.argsort sorts ascending. We use negative scores to sort descending (best first).
    company_prefs = np.argsort(-worker_scores_for_companys, axis=1)
    
    # 3. Workers ranking companys
    # Base preference is company_prestige, plus the worker's subjective noise
    worker_noise = np.random.normal(loc=0, scale=noise_level, size=(n_workers, n_companys))
    company_scores_for_workers = company_prestige + worker_noise
    
    worker_prefs = np.argsort(-company_scores_for_workers, axis=1)
    
    return worker_prefs, company_prefs

# Initialize the 500x500 market
worker_preferences, company_preferences = generate_market_preferences(500, 500)

print(f"Worker 0's top 5 choices: {worker_preferences[0, :5]}")
print(f"company 0's top 5 choices: {company_preferences[0, :5]}")