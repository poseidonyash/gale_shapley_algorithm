import numpy as np 
import numpy as np 

def generate_market_preferences(n_workers=500, n_companys=500, noise_level=0.15):
    np.random.seed(42)
    
    # 1. Hidden Variables
    worker_quality = np.random.normal(loc=0.5, scale=0.15, size=n_workers)
    company_prestige = np.random.normal(loc=0.5, scale=0.15, size=n_companys)
    
    # 2. Rankings
    company_noise = np.random.normal(loc=0, scale=noise_level, size=(n_companys, n_workers))
    worker_scores_for_companys = worker_quality + company_noise
    company_prefs = np.argsort(-worker_scores_for_companys, axis=1)
    
    worker_noise = np.random.normal(loc=0, scale=noise_level, size=(n_workers, n_companys))
    company_scores_for_workers = company_prestige + worker_noise
    worker_prefs = np.argsort(-company_scores_for_workers, axis=1)
    
    # 3. TRANSLATION STEP: Convert the NumPy arrays into pop-able dictionaries
    workers_dict = {}
    for i in range(n_workers):
        # Map integer 5 to string "company 5" and convert to a standard Python list
        workers_dict[f"worker {i}"] = [f"company {j}" for j in worker_prefs[i]]
        
    companies_dict = {}
    for i in range(n_companys):
        companies_dict[f"company {i}"] = [f"worker {j}" for j in company_prefs[i]]
    
    return workers_dict, companies_dict

workers_preference, companies_preference = generate_market_preferences(500, 500)