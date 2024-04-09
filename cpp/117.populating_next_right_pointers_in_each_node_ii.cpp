#include <queue>

// Definition for a Node.
class Node {
 public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
 public:
    Node* connect(Node* root) {
        if (!root) {
            return nullptr;
        }

        auto q = std::queue<Node*>{};
        q.push(root);

        while (!q.empty()) {
            int len = q.size();
            Node* previous = nullptr;

            for (int i = 0; i < len; ++i) {
                if (previous) {
                    q.front()->next = previous;
                }

                if (q.front()->right) {
                    q.push(q.front()->right);
                }
                if (q.front()->left) {
                    q.push(q.front()->left);
                }
                if (len > 1) {
                    previous = q.front();
                }
                q.pop();
            }
        }
        return root;
    }
};
