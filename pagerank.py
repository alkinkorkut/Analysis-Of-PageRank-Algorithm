def calculate_pagerank(links, damping_factor=0.85, epsilon=1e-8, max_iterations=100):
    num_pages = len(links)
    initial_rank = 1.0 / num_pages
    ranks = [initial_rank] * num_pages
    for _ in range(max_iterations):
        new_ranks = [(1 - damping_factor) / num_pages] * num_pages
        print(new_ranks)
        for i, page_links in enumerate(links):
            for link in page_links:
                new_ranks[link] += damping_factor * ranks[i] / len(page_links)

        diff = sum(abs(new_rank - rank) for new_rank, rank in zip(new_ranks, ranks)) 
        ranks = new_ranks

        if diff < epsilon:
            break

    return ranks

# Example usage
links = [[1, 2], [2, 3], [0, 3], [2]]
pageranks = calculate_pagerank(links)
print(pageranks)