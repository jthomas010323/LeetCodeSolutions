/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    const cycleSet=new Set();
    if(!head)
        return null
    while(head.next){
        if(cycleSet.has(head))
            return head
        else{
        cycleSet.add(head);
        head=head.next;
        }
    }
    return null
    
};