#include <unordered_map>


 // * Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        int psum = 0;
        std::unordered_map<int, ListNode*>map_psum;
        ListNode *dummy = new ListNode(0, head);
        map_psum[0] = dummy;

        while(head != nullptr) {
            psum += head->val;
            if(map_psum.find(psum) != map_psum.end()) {
                ListNode *start = map_psum[psum];
                ListNode *tmp = start;
                int tmp_psum = psum;
                while(tmp != head){
                    tmp = tmp->next;
                    tmp_psum += tmp->val;
                    if(tmp != head){
                        map_psum.erase(tmp_psum);
                    }
                }
                start->next = head->next;
            }
            else{
                map_psum[psum] = head;
            }
            head = head->next;

        }
        return dummy->next;
    }
};
