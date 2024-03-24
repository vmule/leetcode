
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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* dummy = new ListNode(0, head);
        ListNode* prev = dummy;
        ListNode* current = head;

        while (current && current->next) {
            ListNode* next_pair = current->next->next;
            ListNode* second = current->next;

            second->next = current;
            current->next = next_pair;
            prev->next = second;

            prev = current;
            current = next_pair;
        }
        return dummy->next;
    }
};
