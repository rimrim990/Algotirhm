def solution(gems):
    gmap = {gems[0]: 1}
    gcnt = 1
    answer = [0, len(gems)+1]

    end = 1
    total_cnt = len(set(gems))
    for start in range(len(gems)):
        while end < len(gems) and gcnt < total_cnt:
            if gmap.get(gems[end]) and gmap[gems[end]] > 0:
                gmap[gems[end]] += 1
            else:
                gcnt += 1
                gmap[gems[end]] = 1
            end += 1

        if gcnt == total_cnt and answer[1]-answer[0] > end-start-1:
            answer[0] = start+1
            answer[1] = end

        gmap[gems[start]] -= 1
        if gmap[gems[start]] == 0:
            gcnt -= 1

    return answer