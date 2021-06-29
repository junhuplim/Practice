// note that python set and map implementation differs from cpp
/*
in cpp: there are different maps (same to set --> order allows you to find successors and predecessors)
1) map --> access and retrieve time = O(logN) (implemented as red black trees)
2) unordered maps --> access and retrieve time (O(1)) (hashtable with linked list - same as py)
*/

#include<bits/stdc++.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

void vectorDemo() {
	vector<int> A;
	A.push_back(3);
	A.push_back(2);
	A.push_back(11);
	A.push_back(14);
	sort(A.begin(), A.end()); //nlogn

	bool present = binary_search(A.begin(), A.end(), 3); //logn

	A.push_back(100);
	A.push_back(100);
	A.push_back(100);
	A.push_back(123);
	//2,3,11,14,100,100,100,123,

	auto it = lower_bound(A.begin(), A.end(), 100); //>=  100,100,100,123
	auto it2 = upper_bound(A.begin(), A.end(), 100); //>  123

	cout << *it << " " << *it2 << endl;
	cout << it2-it << endl; //3 count of your bounds

	sort(A.rbegin(), A.rend());

	for (int &x: A) { //by reference (can modify the elements in the array)
		x++;
	}

	for (int x: A) {
		cout << x << " ";
	}

	cout << endl;
}

// sets are implemented as red-black trees (balanced bst) under the hood
// sorted unique values
void setDemo() {
	set<int> S;
	S.insert(1); //nlogn
	S.insert(2);
	S.insert(-1);
	S.insert(-10);

	for (int x : S) {
		cout << x << " ";
	}
	cout << endl; //-10, -1, 1, 2

	auto it = S.find(-1);
	if (it == S.end()) {
		cout << "not present\n";
	} else {
		cout << "present\n";
		cout << *it << endl;
	}

	auto it2 = S.upper_bound(-1); //1
	auto it3 = S.upper_bound(0); //1
}

void mapDemo() {
	map<int, int> A;
	A[1] = 100; //logn
	A[2] = -1;
	A[3] = 200;
	A[100123] = 1;
	A[-1] = 10;

	map<char, int> cnt;
	string x = "junhup";

	for (char c : x) {
		cnt[c]++;
	}

	//retrieve in logn time too (note that this differs for python)
	cout << cnt['u'] << " " << cnt['v'] << endl;
}

void problemDemo() {
	/*
	add [2, 3]
	add [30, 400]
	add [401, 450]
	add [10, 20]
	give me interval 401
	*/
	set<pair<int, int>> S;
	S.insert({401, 450});
	S.insert({2, 3});
	S.insert({30, 400});
	S.insert({10, 20});

	//2, 3
	//10, 20
	//30, 400
	//401, 450

	int point = 1;

	auto it = S.upper_bound({point, INT_MAX});
	if (it == S.begin()) {
		cout << "given point not lying to any interval\n";
		return;
	}

	it--;
	pair<int, int> current = *it;
	if (current.first <= point && point <= current.second) {
		cout << "yes present:" << current.first << " " << current.second << endl;
	} else {
		cout << "given point not lying to any interval\n";
	}

}

int main()
{
	problemDemo();
}