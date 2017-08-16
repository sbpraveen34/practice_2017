#include<iostream>
#include <stdlib.h>

using namespace std;

int main() {
    int n;
    cin>>n;
    int t, u, a=0, b=0;
    int maxlead=0;
    for(int i=0;i<n;i++) {
        cin>>t>>u;
        a = a+t;
        b = b+u;
        if(abs(a-b) > abs(maxlead)) {
            maxlead = a-b;
        }

    }
    if(maxlead > 0) {
        cout<<1<<" ";
    } else {
        cout<<2<<" ";
    }
    cout<<abs(maxlead)<<endl;
}
