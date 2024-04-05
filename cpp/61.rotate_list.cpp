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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) {
            return nullptr;
        }

        if (!head->next) {
            return head;
        }

        int len = 0;
        ListNode* node = head;

        while (node) {
            node = node->next;
            ++len;
        }

        k = k % len;

        ListNode* first_node;
        ListNode* last_node;
        ListNode* previous_node;

        while (k > 0) {
            first_node = head;
            last_node = head;

            while (last_node->next) {
                previous_node = last_node;
                last_node = last_node->next;
            }

            previous_node->next = nullptr;
            last_node->next = first_node;
            head = last_node;
            --k;
        }

        return head;
    }
};
