#include <bits/stdc++.h>
using namespace std;

int N;
vector <vector <int> > G;
vector <bool> visit;

void dfs(int x) {
  visit[x] = 1;
  for (auto y : G[x])
    if (!visit[y]) dfs(y);
}

int main () {
  freopen("input.txt","r",stdin);
  scanf("%d",&N);
  int tot = 0;
  for (int i=0;i<N;++i) {
    int t, a;
    scanf("%d",&t);
    tot += t;
    vector <int> V;
    for (int j=0;j<t;++j) {
      scanf("%d",&a);
      V.push_back(a);
    }
    G.push_back(V);
  }
  printf("tot = %d\n",tot);
  visit = vector<bool>(N, 0);
  dfs(0);
  for (int i=0;i<N;++i)
    if (!visit[i]) {
      printf("FAIL\n");
      break;
    }
  printf("WIN\n");
}
