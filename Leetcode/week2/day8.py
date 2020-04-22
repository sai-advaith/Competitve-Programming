class Solution(object):
    def middleNode(self, head):
        linked_list = [head]
        while linked_list[-1].next:
            linked_list.append(linked_list[-1].next)
        return linked_list[len(linked_list) // 2]