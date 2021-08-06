#include <bits/stdc++.h>
using namespace std;

#define fastio()                                                               \
  ios_base::sync_with_stdio(false);                                            \
  cin.tie(NULL);                                                               \
  cout.tie(NULL)
#define endl "\n"
#define MOD 1000000007
#define INF 1e18
#define all(a) a.begin(), a.end()
#define rep(i, a, n) for (int i = a; i < n; ++i)
#define each(a) for (auto x : a)
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define ff first
#define ss second

typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vp;

#ifndef ONLINE_JUDGE
#define debug(x)                                                               \
  cerr << #x << " ==> ";                                                       \
  _print(x);                                                                   \
  cerr << endl;
#else
#define debug(x)
#endif

template <class T> void _print(T t) { cerr << t; }

template <class T, class V> void _print(pair<T, V> p);
template <class T> void _print(vector<T> v);
template <class T> void _print(set<T> v);
template <class T, class V> void _print(map<T, V> v);
template <class T> void _print(multiset<T> v);
template <class T, class V> void _print(pair<T, V> p) {
  cerr << "{";
  _print(p.ff);
  cerr << ",";
  _print(p.ss);
  cerr << "}";
}
template <class T> void _print(vector<T> v) {
  cerr << "[ ";
  for (T i : v) {
    _print(i);
    cerr << " ";
  }
  cerr << "]";
}
template <class T> void _print(set<T> v) {
  cerr << "[ ";
  for (T i : v) {
    _print(i);
    cerr << " ";
  }
  cerr << "]";
}
template <class T> void _print(multiset<T> v) {
  cerr << "[ ";
  for (T i : v) {
    _print(i);
    cerr << " ";
  }
  cerr << "]";
}
template <class T, class V> void _print(map<T, V> v) {
  cerr << "[ ";
  for (auto i : v) {
    _print(i);
    cerr << " ";
  }
  cerr << "]";
}

int n, m, l, k, p, q, r, s, x, y, z, a, b, c, d;
int sum = 0, ans = 0, total = 0;

void solve() {
  int n;
  cin >> n;
  cout << n;
}

signed main() {

  fastio();
#ifndef ONLINE_JUDGE
  freopen("error", "w", stderr);
#endif
  int t;
  cin >> t;
  /* t = 1; */

  while (t--) {
    solve();
  }
  return 0;
}
