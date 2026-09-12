# Gale Shapley matching algorithm for job seekers and companies hiring

I am currently unemployed and exploring various algorithms that employers might implement to find the best possible employee and like wise for employees to find the company they prefer the most.

I created the algorithm using the stable matching problem and compared it with your basic greedy algorithm that just prioritizes candidates that apply earlier. 

## Results

### Greedy (First-Come, First-Served) Results: 
- Fill Rate: 85.2%
- Total GMV: $41,122,141.14
- Avg Worker Rank: 35.86
- Avg Company Rank: 277.85

### Gale-Shapley Results:
- Fill Rate: 99.8%
- Total GMV: $49,893,493.99
- Avg Worker Rank: 112.54
- Avg Company Rank: 72.87

Gale-Shapley implementation captured an additional $8.77 million in transaction volume and pushed the fill rate to near-perfect equilibrium. In the Greedy model, early applicants snatch up high-budget companies regardless of their own reserve wage. This exhausts the market's available capital early, stranding the top-tier, high-wage talent later in the queue. By allowing deferred acceptance, the algorithm acts as a highly efficient order book, continually reallocating capital until supply and demand match at optimal clearing prices.

### Survivorship bias:

At first glance, the Greedy algorithm seems vastly superior for workers, granting them an average rank of 35 versus Gale-Shapley's 112. That 35 average only accounts for the 85.2% of workers who actually secured a job. The 15% who failed to match aren't included in this metric thus making the results more appealing. 

![Greedy vs Gale-Shapley distribution](images/greedy-vs-gale-shapley.png)
C:\Users\praja\Desktop\yp\gale_shapley_algorithm\images\greedy vs gale-shapley distribution.png
