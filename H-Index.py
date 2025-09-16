def hIndex(citations):
    citations.sort(reverse=True)
    for i, citation_count in enumerate(citations):
        if citation_count >= i + 1:
            continue
        else:
            return i
    return len(citations)
