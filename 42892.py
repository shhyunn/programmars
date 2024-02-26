class Node():
    def __init__(self,x):
        self.num = x
        self.left = None
        self.right = None

    def value(self):
        return self.num
    
    def set_left(self,node):
        self.left = node

    def get_left(self):
        return self.left

    def set_right(self,node):
        self.right = node
    
    def get_right(self):
        return self.right
    

def solution(nodeinfo):
    #카카오프렌즈를 두팀으로, 같은 곳을 다른 순서로 방문하여 먼저 순회를 마친 팀이 승리
    nodes = [k[0] for k in nodeinfo] #인덱스가 x에 대한 고유번호

    nodeinfo = sorted(nodeinfo, key=lambda x:x[1],reverse=True)
    root = Node(nodeinfo[0][0])
    curr = root
    if len(nodeinfo) > 1:
        for x,y in nodeinfo[1:]:
            node = Node(x)
            curr = root
            while curr:
                if curr.value() > x:
                    if curr.get_left() == None:
                        curr.set_left(node)
                        break
                    else:
                        curr = curr.get_left()
                else:
                    if curr.get_right() == None:
                        curr.set_right(node)
                        break
                    else:
                        curr = curr.get_right()
    
    def preorder(node):
        if node == None:
            return []
        return [nodes.index(node.value())+1] + preorder(node.get_left()) + preorder(node.get_right())
            
    #postorder
    def postorder(node):
        if node == None:
            return []
        return postorder(node.get_left()) + postorder(node.get_right()) + [nodes.index(node.value())+1]
    return [preorder(root),postorder(root)]
# print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
print(solution([[0,0]]))