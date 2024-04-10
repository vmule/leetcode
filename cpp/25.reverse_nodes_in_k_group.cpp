// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 public:
    ListNode* getKNode(ListNode* node, int k) {
        while (node && k > 0) {
            node = node->next;
            --k;
        }
        return node;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* groupPrev = dummy;

        while (true) {
            ListNode* kth = getKNode(groupPrev, k);
            if (!kth) {
                break;
            }
            ListNode* groupNext = kth->next;
            ListNode* previous = kth->next;
            ListNode* current = groupPrev->next;

            while (current != groupNext) {
                ListNode* tmp = current->next;
                current->next = previous;
                previous = current;
                current = tmp;
            }
            ListNode* tmp = groupPrev->next;
            groupPrev->next = kth;
            groupPrev = tmp;
        }
        return dummy->next;
    }
};
