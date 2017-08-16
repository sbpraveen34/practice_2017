#include<iostream>
#include <vector>
using namespace std;

vector<unsigned char> intToBytes(int paramInt)
{
     vector<unsigned char> arrayOfByte(4);
     for (int i = 0; i < 4; i++)
         arrayOfByte[3 - i] = (paramInt >> (i * 8));
     return arrayOfByte;
}

int main() {
    vector<unsigned char> b;
    b = intToBytes(300);
    for(int i=0;i<b.size();i++) {
        cout<<b[i];
    }
    cout<<endl;
    return 0;
}
