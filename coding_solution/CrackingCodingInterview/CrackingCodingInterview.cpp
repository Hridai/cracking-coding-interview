// CrackingCodingInterview.cpp : main function here.

#include <iostream>
#include "Chapter1.h"

using namespace std;

int main(int argc, char* argv[])
{
    if (argc < 3) {
        cout << "Insufficient arguments provided." << endl;
        return 1;
    }

    // access the cmd-line args
    string param1 = argv[1];
    string param2 = argv[2];

    cout << "Parameter 1: " << param1 << endl;
    cout << "Parameter 2: " << param2 << endl;

    std::cout << "Hello World!\n";
    Chapter1 c1;
    int x = c1.run();
    std::cout << x;

    return 0;
}
