#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n, h;
    cin>>n>>h;
    vector<int> a;
    int k;
    for(int _=0;_<n;_++) {
        cin>>k;
        a.push_back(k);
    }
    int p=0, l=0;
    while(true) {
        cin>>k;
        if(k== 0)
            break;
        if(k == 1) {
            if(p > 0)
                p--;
            continue;
        }
        if(k == 2) {
            if(p < n-1) {
                p++;
            }
            continue;
        }
        if(k == 3) {
            if(a[p] > 0) {
                a[p] = a[p]-1;
            }
            continue;
        }
        if(k == 4) {
            if(a[p] < h) {
                a[p] = a[p]+1;
            }
            continue;
        }
    }

    for(int i=0;i<n;i++) {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}
