import numpy as np

def calculate_pagerank(links, damping_factor=0.85, epsilon=1e-8, max_iterations=100):
    num_pages = len(links)
    initial_rank = 1.0 / num_pages
    ranks = np.full((num_pages,1),initial_rank) # We initialize PageRanks with 1 / num_pages
    A = np.zeros((len(links),len(links)))   
    for i in range(len(links)):
        for j in range(len(links[i])):
            A[i][links[i][j]] += ((1/len(links[i])))
    for _ in range(max_iterations):


        new_ranks = ((1 - damping_factor) / num_pages) + damping_factor * np.matmul(A.T, ranks)
        diff = np.sum(np.abs(new_ranks - ranks))
        ranks = new_ranks
        if diff < epsilon:
            break
        if (_ <=3):
            print(ranks)
    return ranks

# Example usage
links = [[1, 2], [2, 3], [0, 3], [2]]
pageranks = calculate_pagerank(links)
print("Final Ranks: ")
print(pageranks) 