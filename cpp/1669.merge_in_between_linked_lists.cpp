
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {

        ListNode* tail2 = list2;
        while (tail2 && tail2->next) {
            tail2 = tail2->next;
        }

        int i = 0;
        ListNode* node_a;
        ListNode* node_b;
        ListNode* node = new ListNode(0, list1);

        while (node && node->next){
            if (i == a) {
                node_a = node;
            } else if (i == b + 1){
                node_b = node->next;
                break;
            }
            node = node->next;
            ++i;
        }
        node_a->next = list2;
        tail2->next = node_b;

        return list1;
    }
};
