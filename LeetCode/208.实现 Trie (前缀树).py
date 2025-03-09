class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        """
        root.son = {a:Node(), b:Node()...}
        """
        self.son = dict() # 该节点的下一节点
        self.end = False # 表示该节点是否为终止节点


### 可以理解为26叉树
class Trie:
    def __init__(self):
        self.root = Node() # 根节点为空

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True # 最后一个节点为终止节点

    def find(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.son:
                return 0 # 不存在word及其前缀
            cur = cur.son[c]
        # 存在word这一个单词
        if cur.end:
            return 2
        # 存在前缀word 但不存在word单词
        else:
            return 1

    def search(self, word: str) -> bool:
        return self.find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0

"""
作者：灵茶山艾府
链接：https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/2993894/cong-er-cha-shu-dao-er-shi-liu-cha-shu-p-xsj4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



设计
字典树
哈希表
字符串
"""