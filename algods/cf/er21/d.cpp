#include<bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;k<n?i<n:i>n;k<n?i+=1:i-=1)
#define ll long long
#define si(x)	scanf("%d",&x)
#define sl(x)	scanf("%lld",&x)
#define pi(x)	printf("%d\n",x)
#define pl(x)	printf("%lld\n",x)
#define ps(s)	printf("%s\n",s)
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define clr(x) memset(x, 0, sizeof(x))
#define sortall(x) sort(all(x))
#define tr(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pl;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pl>		vpl;
typedef vector<vi>		vvi;

const int mod = 1000000007;
const int N = 3e5, M = N;
//=======================

vi g[N];
// int a[N];

void solve() {
  int n;
	ll s=0, s_prime, x, y;
	cin >> n;
	vector<int> A(n+5);
	for (int i; i<n; i++) cin >> A[i];

	unordered_map<ll, int> first, second;
	s += A[0];
	first[A[0]]++;
	for (int i = 1; i<n; i++) {
		second[A[i]]++;
		s+=A[i];}
	// if sum is odd, return no
	if (s & 1) {cout << "NO\n"; return;}
	s_prime = 0;

	for (int i = 0; i<n; i++) {
		s_prime += A[i];
		if (s_prime == s/2) {
			cout << "YES\n";
			return;
		} else if (s_prime < s/2) {
			y = s/2 - s_prime;
			if (second[y] > 0) {
				cout << "YES\n";
				return;
			}
		} else {
			x = s_prime - s/2;
			if (first[x] > 0) {
				cout << "YES\n";
				return;
			}
		}
		first[A[i+1]]++;
		second[A[i+1]]--;
	}
	cout << "NO" << endl;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());

    int t = 1;
    // cin >> t;
    while(t--) {
      solve();
    }

    return 0;
}
