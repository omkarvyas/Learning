/*
 * T1.cpp
 *
 *  Created on: Sep 11, 2017
 *      Author: ovyas
 */



#include <iostream>
using namespace std;

int main(){

	enum color {red, green, blue} d;
	float a,b,c;
	register int x;
	a = 10.4;
	b = 2.9;
	c = b/a;
	cout << "c = " << c <<endl;
    cout << "address of x = " << &x <<endl; // It should actually fail as x is register type but it does not fail!

	cout << "size oc char: " << sizeof(char)<< endl;
	cout << "size of int: " << sizeof(int) <<endl;
	cout << "size of short int: " << sizeof(short int) <<endl;
	cout << "size of long int: " << sizeof(long int) <<endl;
	cout << "size of long long: " << sizeof(long long) <<endl;
	cout << "size of float: " << sizeof(float) <<endl;
	cout << "size of double: " << sizeof(double) <<endl;
	cout << "size of wchar_t: " << sizeof(wchar_t) <<endl;

	d = blue;
	cout << "d: " << d << endl;


	return 0;



}
