
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
    void reorderList(ListNode* head) {
        ListNode* fast = head->next;
        ListNode* slow = head;

        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;

        while (second) {
            ListNode* tmp = second->next;
            second->next = prev;
            prev = second;
            second = tmp;
        }

        ListNode* first = head;
        second = prev;

        while (second) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;

            first->next = second;
            second->next = tmp1;
            first = tmp1;
            second = tmp2;
        }
    }
};
