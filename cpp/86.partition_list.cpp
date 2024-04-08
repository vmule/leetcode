
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
    ListNode* partition(ListNode* head, int x) {
        ListNode* left = new ListNode();
        ListNode* right = new ListNode();

        ListNode* ltail = left;
        ListNode* rtail = right;

        ListNode* current = head;
        while (current) {
            if (current->val < x) {
                ltail->next = current;
                ltail = ltail->next;
            } else {
                rtail->next = current;
                rtail = rtail->next;
            }
            current = current->next;
        }

        ltail->next = right->next;
        rtail->next = nullptr;

        return left->next;
    }
};
