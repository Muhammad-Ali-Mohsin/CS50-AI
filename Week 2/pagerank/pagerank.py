import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Adds all the probabilities of choosing a random page
    if len(corpus[page]) == 0:
        probabilities = {page_: 1 / len(corpus) for page_ in corpus}
    else:
        probabilities = {page_: (1 - damping_factor) / len(corpus) for page_ in corpus}

    # Adds the probabilities to each link on the page
    for link in corpus[page]:
        probabilities[link] += damping_factor / len(corpus[page])

    return probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Creates a dictionary keeping count of samples and a starting sample
    sample_count = {page: 0 for page in corpus}
    sample = random.choice(list(corpus))
    
    # Adds to the sample count and generates new samples using the transition model as weights
    for i in range(n):
        sample_count[sample] += 1
        probabilities = transition_model(corpus, sample, damping_factor)
        sample = random.choices(
            population=list(probabilities), 
            weights=list(probabilities[page] for page in probabilities)
            )[0]

    # Returns the PageRank of each page
    return {page: sample_count[page] / n for page in corpus}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    max_change = 1
    threshold = 0.001
    pageranks = {page: 1 / len(corpus) for page in corpus}

    while max_change > threshold:
        max_change = 0
        for page in corpus:
            pagerank = (1 - damping_factor) / len(corpus)
            for page2 in corpus:
                if page in corpus[page2]:
                    pagerank += damping_factor * pageranks[page2] / len(corpus[page2])

            max_change = max(abs(pageranks[page] - pagerank), max_change)
            pageranks[page] = pagerank
    
    print(sum(pageranks[i] for i in pageranks))

    return pageranks


if __name__ == "__main__":
    main()
