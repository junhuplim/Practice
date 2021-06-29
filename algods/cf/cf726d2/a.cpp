#include<bits/stdc++.h>
#define fast_io ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;
#define dbg(x) cout << "ans: " << x << endl
#define cout(x) cout << x << endl

int main()
{
	fast_io;
	int t; cin>>t;
	while(t--)
	{
		int n; cin>>n;
		int a[n], sum=0;
		for (int i=0; i<n; ++i) {cin>>a[i]; sum+=a[i];}
		if (sum<n) { cout(1); }
		else { cout(sum-n); }
	}

	return 0;
}