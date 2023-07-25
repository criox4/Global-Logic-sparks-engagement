class Solution {
    removeLoop(head) {
        let sPtr = head;
        let fPtr = head;
        let loop = null;

        while (fPtr !== null && fPtr.next !== null) {
            sPtr = sPtr.next;
            fPtr = fPtr.next.next;

            if (sPtr === fPtr) {
                loop = sPtr;
                break;
            }
        }

        if (loop === null) {
            return;
        }

        let loopLength = 1;
        let tempPtr = loop.next;
        while (tempPtr !== loop) {
            loopLength++;
            tempPtr = tempPtr.next;
        }

        let ptr1 = head;
        let ptr2 = head;
        for (let i = 0; i < loopLength; i++) {
            ptr2 = ptr2.next;
        }

        while (ptr1 !== ptr2) {
            ptr1 = ptr1.next;
            ptr2 = ptr2.next;
        }

        while (ptr2.next !== ptr1) {
            ptr2 = ptr2.next;
        }

        ptr2.next = null;
    }
}
