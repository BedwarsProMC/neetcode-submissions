class ListNode {
    int val;
    ListNode next;
    
    public ListNode(int val) {
        this(val, null);
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class LinkedList {

    private ListNode head;
    private ListNode tail;

    public LinkedList() {
        ListNode dummy = new ListNode(-1);
        this.head = dummy;
        this.tail = head;
    }

    public int get(int index) {
        int i = 0;
        ListNode cur = head.next;
        while(cur != null) {
            if(i == index) {
                return cur.val;
            }
            i++;
            cur = cur.next;
        }
        return -1;
    }

    public void insertHead(int val) {
        ListNode newNode = new ListNode(val);
        newNode.next = head.next;
        head.next = newNode;
         
        if(newNode.next == null)
            tail = newNode;
    }

    public void insertTail(int val) {
        ListNode newNode = new ListNode(val);

        tail.next = newNode;
        tail = tail.next;

    }

    public boolean remove(int index) {
        int i = 0;

        ListNode cur = head;
        while(i < index && cur != null) {
            i++;
            cur = cur.next;
        }

        if(cur != null && cur.next != null) {
            if(cur.next == tail) {
                tail = cur;
            }
            cur.next = cur.next.next;
            return true;
        }

        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> res = new ArrayList();

        ListNode cur = head.next;
        while(cur != null) {
            res.add(cur.val);
            cur = cur.next;
        }
        return res;


    }
}
