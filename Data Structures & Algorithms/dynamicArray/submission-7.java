class DynamicArray {

    private int capacity;
    private int size;
    private int[] array;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.array = new int[capacity];
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        // if(this.array[i] == 0) {
        //     this.size++;
        // }

        this.array[i] = n;
    }

    public void pushback(int n) {
        if(this.size == this.capacity) {
            this.resize();
        }

        this.array[this.size] = n;
        this.size++;
    }

    public int popback() {
        this.size--;
        int lastElement = this.array[this.size];
        
        this.array[this.size] = 0;

        return lastElement;
    }

    private void resize() {
        this.capacity = this.capacity * 2;
        int[] newArray = new int[this.capacity];

        for(int i = 0; i < array.length; i++) {
            newArray[i] = this.array[i];
        }

        this.array = newArray;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }

}
