def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    if len(scores) > 2 :
        return scores[0:3]
    else :
        return scores
