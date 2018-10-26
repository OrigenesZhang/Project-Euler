#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define ROF(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) FOR(i, 0, (n)-1)
#define all(x) (x).begin(), (x).end()
#define reset(x, y) memset(x, y, sizeof(x))
#define uni(x) (x).erase(unique(all(x)), (x).end());
#define BUG(x) cerr << #x << " = " << (x) << endl
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define _1 first
#define _2 second

#define hash has
const int maxn = 120 * 120;

vector<int> G[maxn];
int mat[maxn], dp[maxn];

inline int hash(int x, int y) {
    return (x - 1) * 100 + (y - 1);
}

int dfs(int u) {
    if (dp[u]) return dp[u];
    int mmax = 0;
    for (int v : G[u]) mmax = max(mmax, dfs(v));
    return dp[u] = mmax + mat[u];
}

int main() {
    FOR(i, 1, 100) FOR(j, 1, i) {
            cin >> mat[hash(i, j)];
            if (i > 1) {
                if (j > 1) G[hash(i - 1, j - 1)].pb(hash(i, j));
                G[hash(i - 1, j)].pb(hash(i, j));
            }
        }
    cout << dfs(hash(1, 1)) << endl;
    return 0;
}
