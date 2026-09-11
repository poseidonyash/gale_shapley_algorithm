import numpy as np 
from data_generator import workers_preference, companies_preference

def greedy_matching(workers_pref, companies_pref):
    matches = {}
    for worker in workers_pref:
        for company in workers_pref[worker]:
            if company in matches:
                pass
            else:
                matches[company] = worker
                break 
    return matches 



