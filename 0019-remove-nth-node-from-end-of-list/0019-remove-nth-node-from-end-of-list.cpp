/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head->next==nullptr||head==nullptr){
            return nullptr;
        }
        ListNode* fast=head;
        ListNode* slow=head;
        ListNode* prev=head;
        for(int i=0; i<n;i++){
            fast=fast->next; }
        while(fast!=nullptr){
            fast=fast->next;
            prev=slow;
            slow=slow->next;
        }
        if(slow==head && n!=1){
            ListNode* temp=head;
            head=temp->next;
            delete temp;
        }
        else{
            prev->next=slow->next;
            slow->next=nullptr;
            delete slow;
        }
        
    return head;
    }
};