// Solution for all-nodes-distance-k-in-binary-tree (C)
// Problem: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
#include <stdio.h>
#include <stblib.h>
#include <string.h>

// TreeNode Structure
typedef struct TreeNode{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

// Queue structure for BFS
typedef struct QueueNode{
    TreeNode *treeNode;
    int distance;
    struct QueueNode *next;
} QueueNode;

typedef struct {
    QueueNode *front;
    QueueNode *rear;
} Queue;

//Function prototypes
void buildParentMap(TreeNode *node, TreeNode *parent, TreeNode **parentMap);
int* distancek(TreeNode *root, TreeNode *target, int k, int *return);
void enqueue(Queue *q, TreeNode *node, int distance);
QueueNode* dequeue(Queue *q);
int isEmpty(Queue *q);

//main solution function
int* distanceK(){


}

int main() {
    printf("Solution for all-nodes-distance-k-in-binary-tree\n");
    return 0;
}

