def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)

    #  scores_sorted = [score for score in sorted(scores)
    #  return scores_sorted[-1]

def personal_top_three(scores):
    scores.sort(reverse= True)
    return scores[0:3]

def sort_highest_to_lowest(scores):
    scores.sort(reverse= True)
    return scores

