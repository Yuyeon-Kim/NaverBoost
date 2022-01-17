# 220113
# 문제: 
# 중복되는 물품은 합쳐서 표시하세요.
# 각 딕셔너리 데이터의 데이터의 키값을 이용해 중복을 확인해보세요.

dict_first = {'사과':30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dict(dict_first: dict, dict_second: dict):
    # TODO
    for k in dict_second.keys():
        if k in dict_first:
            dict_first[k] += dict_second[k]
        else:
            dict_first[k] = dict_second[k]
    return dict_first

print(merge_dict(dict_first, dict_second))

# 출력
# {'사과': 35, '배': 30, '감': 35, '포도': 10, '귤': 25}