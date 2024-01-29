def solution(people, limit):
    answer = len(people)
    people = sorted(people)

    start, end = 0, 0
    while end < len(people) and people[start] + people[end] <= limit:
        end += 1
    if end: end -= 1

    while start < end < len(people):
        if people[start] + people[end] <= limit:
            answer -= 1
            start += 1
        end -= 1

    return answer