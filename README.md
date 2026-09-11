# Gale Shapley matching algorithm for job seekers and companies hiring

I am currently unemployed and exploring various algorithms that employers might implement to find the best possible employee and like wise for employees to find the company they prefer the most.

I created the algorithm using the stable matching problem and compared it with your basic greedy algorithm that just prioritizes candidates that apply earlier. 

## Results

### Greedy (First-Come, First-Served) Results: 
- Avg Worker Rank: 44.20
- Avg Company Rank: 258.52

### Gale-Shapley Results:
- Avg Worker Rank: 24.39
- Avg Company Rank: 106.79

Turns out Gale-Shapley is a great algorithm to implement as a worker is better off and matches with a company of higher preference and it is the same with companies they match with workers they prefer more. 