"""
Task 3: Runner-up score.
Read n, then n scores. Print the second-highest DISTINCT score.
Input is read from standard input (HackerRank style).
"""
import sys


def runner_up(scores):
    distinct = set(scores)                     # a set removes repeated scores
    ordered = sorted(distinct, reverse=True)   # highest first
    return ordered[1]                          # at least 2 distinct scores guaranteed


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = [int(x) for x in data[1:1 + n]]
    print(runner_up(scores))


if __name__ == "__main__":
    main()
