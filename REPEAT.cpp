#include <iostream>
#include <vector>
using namespace std;

int main() {

	int t;
	cin>>t;
	while(t--) {
		int n, k;
		cin>>n;
		int s = 0;
		for(int i=0;i<n;i++) {
			cin>>k;
			s = s ^ k;
		}
		cout<<s<<endl;
	}

	return 0;
}
