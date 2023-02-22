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
    ListNode* deleteMiddle(ListNode* head) {
        if(head==nullptr||head->next==nullptr){
            return nullptr;
        }
        ListNode* fast=head;
        ListNode* slow=head;
        ListNode* prev=head;
        while(fast!=nullptr){
            fast=fast->next;
                if(fast!=nullptr){
                    fast=fast->next;
                }
            else{
                break;
            }
            prev=slow;
            slow=slow->next;
        }
        if(slow==head){
            ListNode* temp=head;
            head=temp->next;
            delete temp;
        }
        else{
            prev->next=slow->next;
            slow->next==nullptr;
            delete slow;
        }
        return head;
    }
};