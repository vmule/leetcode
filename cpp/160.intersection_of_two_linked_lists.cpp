// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
 public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        int lengthA = 0;
        ListNode* nodeA = headA;
        while (nodeA) {
            nodeA = nodeA->next;
            ++lengthA;
        }

        int lengthB = 0;
        ListNode* nodeB = headB;
        while (nodeB) {
            nodeB = nodeB->next;
            ++lengthB;
        }

        if (lengthA > lengthB) {
            int diff = lengthA - lengthB;
            while (headA && diff > 0) {
                headA = headA->next;
                --diff;
            }
        } else if (lengthA < lengthB) {
            int diff = lengthB - lengthA;
            while (headB && diff > 0) {
                headB = headB->next;
                --diff;
            }
        }

        while (headA != headB) {
            headA = headA->next;
            headB = headB->next;
        }

        return headA;
    }
};
