/*
 * T1.cpp
 *
 *  Created on: Sep 11, 2017
 *      Author: ovyas
 */

/*
 * Common problems http://www.learncpp.com/cpp-tutorial/07-a-few-common-cpp-problems/
 *
 * */

#include <iostream>
using namespace std;

void doPrint(){

	cout << "in function doPrint() " <<endl;

}

int return5(){

	return 5;
}

int add(int x, int y){

	return x+y;

}


int multiply(int z, int w){

	return z*w;

}

int doubleNumber(int x){

	return 2*x;

}

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
	/*
	int in_v = 0;
	cout << "Input some value" <<endl;
	cin >> in_v;
	cout << "you input this value: " << in_v <<endl;
	*/
    doPrint();

    //cout << doPrint() << endl; /*doPrint is void returning fuction so such use is illigal*/
    cout << return5 <<endl; //This program will compile, but the function will not be called because the function call is missing parenthesis.
                            //answer depends on compiler, in this case it just returns 1

    cout << "addition of 3 and 5: " << add(3,5) << endl;
    cout << "multiplication of 3 and 5: " << multiply(3,5) << endl;

    cout << "add(add(3,5),2): " << add(add(3,5),2) <<endl;
    cout << "multiply(add(3,5),2): " << multiply(add(3,5),2) <<endl;
    cout << "Double the number 10: " << doubleNumber(10);
    cout << "input number:";
    int in_val = 0;
    cin >> in_val;
    cout << "Double of your number = " << doubleNumber(in_val) << endl;
	return 0;



}
