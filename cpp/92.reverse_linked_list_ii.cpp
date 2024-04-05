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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head) {
            return nullptr;
        }

        if (!head->next) {
            return head;
        }

        ListNode* dummy = new ListNode(0, head);
        ListNode* left_previous = dummy;
        ListNode* current = head;

        int i = 0;
        while (i < left - 1) {
            left_previous = current;
            current = current->next;
            ++i;
        }

        ListNode* previous = nullptr;

        i = 0;
        while (i < (right - left + 1)) {
            ListNode* tmp = current->next;
            current->next = previous;
            previous = current;
            current = tmp;
            ++i;
        }

        left_previous->next->next = current;
        left_previous->next = previous;

        return dummy->next;
    }
};
