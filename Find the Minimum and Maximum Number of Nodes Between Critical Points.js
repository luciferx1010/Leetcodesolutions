/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
var nodesBetweenCriticalPoints = function(head) {
    
    let prev = head, curr = head.next, first = -1, last = -1, min = Infinity, count = 1;
    
    while(curr.next) {
        
        const isExtr = (prev.val < curr.val && curr.val > curr.next.val) || (prev.val > curr.val && curr.val < curr.next.val);
        
        if(isExtr) {
          first = first > -1 ? first : count;
          min = last > -1 ? Math.min(min, count - last) : min;
          last = count;
        }
        prev = curr;
        curr = curr.next;
        count++;
    }
    
    return first === last ? [-1,-1] : [min, last - first];
};