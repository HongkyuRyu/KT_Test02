import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

node = [0] * (n+1)
for i in range(n):
    node[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
    
    rootNode = postorder[postEnd]
    
    # 왼쪽 서브트리
    left = node[rootNode] - inStart
    # 오른쪽 서브트리
    right = inEnd - node[rootNode]
    
    print(rootNode, end=" ")
    preorder(inStart, inStart + left -1, postStart, postStart + left -1)
    preorder(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)
preorder(0, n-1, 0, n-1)
