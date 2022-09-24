#include <iostream>
using namespace std;

int function1(int x)
{
    return 5 + x;
}

int function2(int x, int y){
    return x + y;
}

int main()
{
    cout << function1(3)<< endl;
    cout<< function2(3, 2)<< endl;

    return 0;
}
