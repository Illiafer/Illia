#include <iostream>
#include <string>
using namespace std;

class Person {
private:
    int year;
    string name;
    string city;

public:
    Person() {
        year = 0;
        name = "Unknown";
        city = "Unknown";
    }

    Person(int y, string n, string c) {
        year = y;
        name = n;
        city = c;
    }

    void get_info() {
        cout << "Year: " << year << ", Name: " << name << ", City: " << city << endl;
    }
};

int main() {
    Person p(2009, "Illia", "Donetsk");
    p.get_info();

    return 0;
}
