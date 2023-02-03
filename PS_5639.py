# 루트노드
# 왼쪽 서브 트리 = 루트 노드보다 작은 원소
# 오른쪽 서브 트리 = 루트 노드보다 큰 원소
# 전위 순회한 결과: 50 30 24 5 28 45 98 52 60
# 50 : 루트 노드, [30, 24 , 5, 29, 45]: 왼쪽 서브트리, [98, 52, 60]: 오른쪽 서브 트리

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > preorder[start]:
            mid = i
            break
    postorder(start+1, mid-1) # 왼쪽 서브트리
    postorder(mid, end) # 오른쪽 서브트리
    print(preorder[start]) # 루트 노드
    
postorder(0, len(preorder)-1)