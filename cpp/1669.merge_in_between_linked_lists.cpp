#include <cassert>
#include <chrono>
#include <iostream>
#include <vector>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

// Function to create a list from a vector
ListNode* vectorToList(const std::vector<int>& v) {
    ListNode* head = nullptr;
    ListNode* tail = nullptr;

    for (int num : v) {
        ListNode* new_node = new ListNode(num);
        if (tail) {
            tail->next = new_node;
        } else {
            head = new_node;
        }
        tail = new_node;
    }

    return head;
}

// Function to compare two linked lists
bool areListsEqual(ListNode* l1, ListNode* l2) {
    while (l1 && l2) {
        if (l1->val != l2->val) {
            return false;
        }
        l1 = l1->next;
        l2 = l2->next;
    }
    return l1 == nullptr && l2 == nullptr;
}

// Deallocate the memory used by the list
void freeList(ListNode* head) {
    while (head) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

/*
 * You are given two linked lists: list1 and list2 of sizes n and m
 * respectively. Remove list1's nodes from the ath node to the bth node, and put
 * list2 in their place.
 */
class Solution {
 public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        // Find the node just before position 'a'
        ListNode* prev_a = nullptr;
        ListNode* curr = list1;
        for (int i = 0; i < a; ++i) {
            prev_a = curr;
            curr = curr->next;
        }

        // Find the node just after position 'b'
        ListNode* post_b = curr;
        for (int i = a; i <= b; ++i) {
            post_b = post_b->next;
        }

        // Find the last node of list2
        ListNode* tail2 = list2;
        while (tail2->next) {
            tail2 = tail2->next;
        }

        // Connect the 'prev_a' node to the start of list2
        if (prev_a != nullptr) {
            prev_a->next = list2;
        } else {
            // If 'a' is 0, list2 becomes the new head of merged list
            list1 = list2;
        }

        // Connect the end of list2 to the 'post_b' node
        tail2->next = post_b;

        return list1;
    }
};

int main() {
    // Test input
    std::vector<int> list1Vec = {0, 1, 2, 3, 4, 5, 6};
    std::vector<int> list2Vec = {1000000, 1000001, 1000002, 1000003, 1000004};
    std::vector<int> expectedVec = {0,       1,       1000000, 1000001,
                                    1000002, 1000003, 1000004, 6};
    unsigned a = 2, b = 5;

    // Create linked lists from the vectors
    ListNode* list1 = vectorToList(list1Vec);
    ListNode* list2 = vectorToList(list2Vec);
    ListNode* expected = vectorToList(expectedVec);

    // Check for correctness
    Solution solution;
    ListNode* mergedList = solution.mergeInBetween(list1, a, b, list2);

    // Check if the output is as expected
    assert(areListsEqual(mergedList, expected));

    std::cout << "Solution works!" << std::endl;

    freeList(mergedList);

    // Warm-up phase before micro-benchmark
    for (int i = 0; i < 10; ++i) {
        ListNode* list1 = vectorToList(list1Vec);
        ListNode* list2 = vectorToList(list2Vec);

        Solution solution;
        ListNode* mergedList = solution.mergeInBetween(list1, a, b, list2);
        freeList(mergedList);
    }

    // Actual measurement
    const int numTrials = 100000;
    long long totalTime = 0;

    for (int i = 0; i < numTrials; ++i) {
        ListNode* list1 = vectorToList(list1Vec);
        ListNode* list2 = vectorToList(list2Vec);

        auto start = std::chrono::high_resolution_clock::now();

        Solution solution;
        ListNode* mergedList = solution.mergeInBetween(list1, a, b, list2);

        auto end = std::chrono::high_resolution_clock::now();
        totalTime +=
            std::chrono::duration_cast<std::chrono::nanoseconds>(end - start)
                .count();

        freeList(mergedList);
    }

    long long averageTime = totalTime / numTrials;

    std::cout << "Average execution time over " << numTrials
              << " trials: " << averageTime << " nanoseconds" << std::endl;

    return 0;
}
