// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 private:
    ListNode* reverseList(ListNode* head) {
        ListNode* previous = nullptr;
        ListNode* current = head;

        while (current) {
            ListNode* tmp = current->next;
            current->next = previous;
            previous = current;
            current = tmp;
        }

        return previous;
    }

 public:
    ListNode* removeNodes(ListNode* head) {
        head = reverseList(head);
        ListNode* current = head;
        int current_max = current->val;

        while (current->next) {
            if (current->next->val < current_max) {
                current->next = current->next->next;
            } else {
                current = current->next;
                current_max = current->val;
            }
        }
        return reverseList(head);
    }
};
