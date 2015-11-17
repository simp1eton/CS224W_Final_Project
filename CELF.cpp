#include <bits/stdc++.h>
using namespace std;

typedef long long int LL;
const int INF = 1000000000;
vector <vector <int> > G;
vector <vector <LL> > dist;
vector <LL> delta, cost;
int N;
LL budget;
bool uniCost; 

struct celf_cmp {
  bool operator() (int a, int b) {
    LL v1 = (uniCost) ? delta[a] : delta[a] * cost[b];
    LL v2 = (uniCost) ? delta[b] : delta[b] * cost[a];
    if (v1 != v2) return v1 < v2;
    return a < b;
  }
};

LL eval(set <int> A) {
  LL ret = 0;
  for (int i=0;i<N;++i) {
    LL cur = 0;
    for (auto a : A) cur = max(cur, dist[a][i]);
    ret += cur;
  }
  return ret;
}

void preprocess() {
  dist.clear();
  queue <int> q;
  for (int i=0;i<N;++i) {
    vector <LL> V(N,INF);
    q.push(i);
    V[i] = 0;
    while (!q.empty()) {
      int x = q.front();
      q.pop();
      for (auto y : G[x])
        if (V[y] == INF) {
          V[y] = V[x] + 1;
          q.push(y);
        }
    }
    dist.push_back(V);
  }
}

void read(string filename) {
  FILE *fin = fopen(filename.c_str(), "r");
  fscanf(fin, "%d",&N);
  for (int i=0;i<N;++i) {
    delta.push_back(0);
    vector <int> edges;
    int K, t;
    fscanf(fin, "%d",&K);
    for (int j=0;j<K;++j) {
      fscanf(fin, "%d",&t);
      edges.push_back(t);
    }
    G.push_back(edges);
  }
  fscanf(fin, "%lld",&budget);
  fclose(fin);
}

set<int> lazyForward(bool isUniCost, set<int> init = set<int>()) {
  uniCost = isUniCost;
  set <int, celf_cmp> remaining;
  if (init.size() == 0)
    for (int i=0;i<N;++i) remaining.insert(i);
  else
    for (int i : init) remaining.insert(i);
  for (auto s : remaining) delta[s] = INF;
  LL remainingBudget = budget;
  set <int> ret;
  while (remainingBudget > 0) {
    if (remaining.empty()) break;
    LL curCost = eval(ret);
    int cur;
    while (true) {
      cur = *remaining.begin();
      remaining.erase(cur);
      if (uniCost || cost[cur] <= remainingBudget) ret.insert(cur);
      else continue;
      LL newCost = eval(ret);
      ret.erase(cur);
      if (newCost - curCost < delta[cur]) {
        delta[cur] = newCost - curCost;
        remaining.insert(cur);
      }
      else break; 
    }
    remainingBudget -= (uniCost) ? 1 : cost[cur];
    ret.insert(cur);
  }
  return ret;
}

set<int> CELF() {
  preprocess();
  set<int> A = lazyForward(1);
  set<int> B = lazyForward(0);
  return (eval(A) < eval(B)) ? A : B;
}

int main () {
  string s;
  cin >> s;
  read(s);
  set <int> sol = CELF();
}
