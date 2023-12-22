def insert_and_find_median(seq, elem):
    i = len(seq)
    while i > 0 and seq[i - 1] > elem:
        seq.append(seq[i - 1])
        i -= 1
    seq.append(elem)

def find_median_sum(n, seq):
    sorted_seq = []
    median_sum = 0

    for i in range(n):
        insert_and_find_median(sorted_seq, seq[i])
        median_sum += (sorted_seq[i // 2] + sorted_seq[(i + 1) // 2]) / (2 - i % 2)

    return median_sum

N = int(input())
X = list(map(int, input().split()))

result = find_median_sum(N, X)
print(result)