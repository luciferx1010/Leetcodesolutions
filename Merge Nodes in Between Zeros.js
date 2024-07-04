/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var mergeNodes = function(head) {
    let prev=head,cur= head.next
    
    while(cur){
        
        if(cur.val==0){
            if(!cur.next){
                prev.next=null
            }
            prev=cur
        }else{
            prev.val+=cur.val
            prev.next=cur.next
           
        }
         cur=cur.next
    }
    return head
};