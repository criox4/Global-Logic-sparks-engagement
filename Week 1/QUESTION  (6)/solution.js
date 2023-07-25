class MyStack {
    constructor() {
        this.stack = [];
        this.minStack = [];
    }

    push(x) {
        this.stack.push(x);

        if (this.minStack.length === 0 || x <= this.getMin()) {
            this.minStack.push(x);
        }
    }

    pop() {
        if (this.stack.length === 0) {
            return -1;
        }

        const popped = this.stack.pop();

        if (popped === this.getMin()) {
            this.minStack.pop();
        }

        return popped;
    }

    getMin() {
        if (this.minStack.length === 0) {
            return -1;
        }

        return this.minStack[this.minStack.length - 1];
    }
}
