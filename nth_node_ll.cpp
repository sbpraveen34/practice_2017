#include<iostream>

using namespace std;

struct node {
    int data;
    node* next;
};

node* insertNode(int data, node *head) {
    node *temp = new node();
    temp->data = data;
    temp->next = head;
    head = temp;
    return head;
}

int main() {
    int n, k, a;
    cin>>n;
    cin>>k;
    node *head = new node();
    head->data = 0;
    head->next = NULL;
    for (int i=0;i<k;i++) {
        cin>>a;
        head = insertNode(a, head);
    }
    node *temp = head;
    while(temp) {
        cout<<temp->data<<endl;
        temp = temp->next;
    }
    cout<<head->data<<endl;
}
