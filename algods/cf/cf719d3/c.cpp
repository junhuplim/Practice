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

void solve() {
  int a[100][100];
  int i, j, n, m;
  int c = 1;
  cin>>n;
  if (n==1) cout<<"1\n";
  else if (n==2) cout<<"-1\n";
  else {
    fo(i, n) fo(j, n) {
      if ((i+j) % 2 == 0) {
        a[i][j] = c;
        ++c;
      }
    }
    fo(i, n) fo(j, n) {
      if ((i+j) % 2 == 1) {
        a[i][j] = c;
        ++c;
      }
    }
    fo(i, n) {
      fo(j, n) {
        cout << a[i][j] << " ";
      }
      cout << "\n";
    }
  }


}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());

    int t = 1;
    cin >> t;
    while(t--) {
      solve();
    }

    return 0;
}
