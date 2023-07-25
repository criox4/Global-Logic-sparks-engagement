class MyStack {
    constructor() {
        this.top = null;
    }

    /**
     * @param {number} a
     */
    push(a) {
        const newNode = {
            data: a,
            next: null
        };

        if (this.top === null) {
            this.top = newNode;
        } else {
            newNode.next = this.top;
            this.top = newNode;
        }
    }

    /**
    */
    pop() {
        if (this.top === null) {
            return -1;
        } else {
            const poppedElement = this.top.data;
            this.top = this.top.next;
            return poppedElement;
        }
    }
}
