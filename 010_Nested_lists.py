# The link to the challenge: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    records = []
    # Taking an input from a user
    for _ in range(int(input())):# Removing all records with scores equals to minimal
        name = input()
        score = float(input())
        records.append([name, score])
    # Finding the minimal score
    min_score = min(records, key = lambda score: score[1])
    # Removing all records with scores equal to the minimal score
    for i in range(sum(i.count(min_score[1]) for i in records)):
        for name, score in records:
            if score == min_score[1]:
                records.remove([name, score])
    # Finding the second minimal score
    second_min_score = min(records, key = lambda score: score[1])
    # Printing all records equal to the second minimal score sorted alphabetically
    second_min_score = sorted([name for name, score in records if score == second_min_score[1]])
    print(*second_min_score, sep='\n')
