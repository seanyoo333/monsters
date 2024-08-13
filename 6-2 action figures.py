def read_boxes(n):
    """n은 읽어야 하는 상자수, 각 상자는 액션 피규어의 높이를 담은 리스트"""
    boxes = []
    for i in range(n):
        box = input().split()
        box = list(map(int, box[1:]))  # Convert all elements except the first to integers
        boxes.append(box)
    return boxes

def box_ok(box):
    """box는 해당 상자 내부의 액션 피규어들의 높이를 담은 리스트이고,
    True를 반환하면 상자 내 액션 피규어들의 높이의 순서가 작아지지 않는 것이고,
    False는 그렇지 않은 것이다"""

    for i in range(len(box) - 1):
        if box[i] > box[i + 1]:
            return False
    return True

def all_boxes_ok(boxes):
    """boxes는 상자들의 리스트, 각 상자는 액션피규어 높이들의 리스트
    상자내의 액션 피규어 높이가 점점작아지지 않으면 True를 반환, 그렇지 않으면 False"""
    for box in boxes:
        if not box_ok(box):
            return False
    return True

def boxes_endpoints(boxes):
    """각각 두 개의 값이 있는 리스트들을 값으로 갖는 리스트를 반환. 두 개의 값은 상자의 가장 왼쪽과 가장 오른쪽 액션 피규어의 높이"""
    endpoints = []
    for box in boxes:
        endpoints.append([box[0], box[-1]])
    return endpoints

def all_endpoints_ok(endpoints):
    """endpoints는 피규어의 높이로 정렬되어야 함
     endpoints가 순서대로 정리가 가능한 상자면 True, 그렇지 않으면 False"""
    maximum = endpoints[0][1]
    for i in range(1, len(endpoints)):
        if endpoints[i][0] < maximum:
            return False
        maximum = endpoints[i][1]
    return True

# 입력을 읽음
n = int(input())
boxes = read_boxes(n)

# 모든 상자가 정상인지 확인
if not all_boxes_ok(boxes):
    print('NO')
else:
    endpoints = boxes_endpoints(boxes)
    endpoints.sort()

    if all_endpoints_ok(endpoints):
        print('YES')
    else:
        print('NO')
