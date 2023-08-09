from collections import deque
def solution(skill, skill_trees):
    answer = 0

    for trees in skill_trees:
        treeIdx = 0
        trees = deque(trees)
        while trees:
            if trees[0] not in skill:
                trees.popleft()
            elif trees[0] == skill[treeIdx]:
                trees.popleft()
                treeIdx += 1
            else:
                break
        if not trees: answer += 1

    return answer