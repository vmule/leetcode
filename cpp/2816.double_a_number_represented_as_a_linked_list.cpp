// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
private:
  ListNode *reverseList(ListNode *head) {
    ListNode *previous = nullptr;
    ListNode *current = head;

    while (current) {
      ListNode *tmp = current->next;
      current->next = previous;
      previous = current;
      current = tmp;
    }

    return previous;
  }

public:
  ListNode *doubleIt(ListNode *head) {
    head = reverseList(head);
    ListNode *current = head;

    int reminder = 0;
    while (current) {
      current->val = (current->val * 2) + reminder;
      reminder = int(current->val) / 10;
      if (current->val > 9) {
        current->val = current->val % 10;
      }
      if (current->next == nullptr && reminder > 0) {
        current->next = new ListNode(reminder, nullptr);
        current = current->next;
      }
      current = current->next;
    }
    return reverseList(head);
  }
};
