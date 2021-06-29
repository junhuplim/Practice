#include<bits/stdc++.h>
#define fast_io ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;
#define l long
#define ll long long
#define dbg(x) cout << "ans: " << x << endl
#define cout(x) cout << x << endl
#define cout_vector(x) for (ll i=0; i<x.size(); ++i) {cout << x[i] << " "}

int main()
{
	fast_io;
	int t; cin>>t;
	while(t--)
	{
		ll n; cin>>n;
		ll a[n];
		vector<ll> v;
		for(int i=0; i<n; i++) {cin>>a[i]; v.push_back(a[i]);}
		sort(v.begin(), v.end());
		ll m=v[1]-v[0];
		ll b=1;
		ll c=0;
		for (ll i=1; i<n-1; ++i){
			if(m > v[i+1]-v[i]){
				m=v[i+1]-v[i];
				b=i+1;
				c=i;
			}
		}
		if (v.size()==2) {
			for (ll i=0; i<v.size(); ++i){
				cout<<v[i]<<" ";
			}
		} else {
			for (ll i=b; i<n; ++i){
				cout<<v[i]<<" ";
			}
			for (ll i=0; i<c+1; ++i) {
				cout<<v[i]<<" ";
			}
		}
		cout<<"\n";
	}

	return 0;
}