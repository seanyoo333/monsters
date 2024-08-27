def ordinal(n):
    """Convert an integer into its ordinal representation"""
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def solve_datasets(datasets):
    results = []

    for i, (m, k, words) in enumerate(datasets):
        # Count word frequencies
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # Sort words by frequency (desc) and then alphabetically (asc)
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

        # Determine the k-th most common frequency
        if k > len(sorted_words):
            results.append(f"{ordinal(k)} most common word(s):")
            results.append("")  # blank line for no k-th most common word
            continue

        target_frequency = sorted_words[k-1][1] if k <= len(sorted_words) else None

        results.append(f"{ordinal(k)} most common word(s):")

        if target_frequency is not None:
            # Collect all words with the k-th most common frequency
            kth_common_words = [word for word, count in sorted_words if count == target_frequency]
            results.extend(kth_common_words)

        results.append("")  # blank line after each dataset

    return results

# Read input
n = int(input().strip())
datasets = []

for _ in range(n):
    m, k = map(int, input().strip().split())
    words = [input().strip() for _ in range(m)]
    datasets.append((m, k, words))

# Solve and output results
results = solve_datasets(datasets)
for result in results:
    print(result)
