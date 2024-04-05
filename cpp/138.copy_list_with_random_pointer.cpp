#include <unordered_map>
// Definition for a Node.
class Node {
 public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
 public:
    Node* copyRandomList(Node* head) {
        std::unordered_map<Node*, Node*> mappings;

        Node* node = head;
        while (node) {
            Node* new_node = new Node(node->val);
            mappings[node] = new_node;
            node = node->next;
        }

        node = head;
        while (node) {
            mappings[node]->next = mappings[node->next];
            mappings[node]->random = mappings[node->random];
            node = node->next;
        }

        Node* new_head = mappings[head];
        return new_head;
    }
};
