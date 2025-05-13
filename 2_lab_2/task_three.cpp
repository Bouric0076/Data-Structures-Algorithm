class Node {
public:
    Student data;
    Node* next;

    Node(Student s) : data(s), next(NULL) {}
};

class LinkedList {
private:
    Node* head;

public:
    LinkedList() : head(NULL) {}

    void add(Student s) {
        Node* newNode = new Node(s);
        newNode->data.set_grade(s.get_grade());  // Grade already calculated
        newNode->next = head;
        head = newNode;
    }

    void print_all() {
        Node* temp = head;
        while (temp != NULL) {
            temp->data.print_info();
            temp = temp->next;
        }
    }
};
