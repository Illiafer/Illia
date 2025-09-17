#include <iostream>
using namespace std;

int main() {
    float num1, num2,res;
    cout << "Enter first  num1: ";
    cin >> num1;
    cout << "Enter first  num2: ";
    cin >> num2;

    char math;
    cout << "Enter first math symbol: ";
    cin >> math;

    if (math == '+')
        res = num1 + num2;
    else if (math == '-')
        res = num1 - num2;
    else if (math == '*')
        res = num1 * num2;
    else if (math == '/')
        res = num1 / num2;
    cout << "Result: " << res << endl;


    return 0;
}
