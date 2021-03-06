#include <iostream>
#include <cstdio>
#include <set>
#include <unistd.h>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
#include <ctime>
using namespace std;

typedef double LF;
typedef long long int LL;
const int INF = 1000000000, NUM_ITERS = 10;
vector <vector <int> > G;
vector <vector <LL> > dist;
vector <LL> delta, cost;
int N;
LL budget;
bool uniCost; 
clock_t start_time; 

struct celf_cmp {
  bool operator() (int a, int b) {
    LL v1 = (uniCost) ? delta[a] : delta[a] * cost[b];
    LL v2 = (uniCost) ? delta[b] : delta[b] * cost[a];
    if (v1 != v2) return v1 > v2;
    return a < b;
  }
};

LL eval(set <int> &A) {
  if (A.size() == 0) return -INF;
  LL ret = 0;
  for (int i=0;i<N;++i) {
    LL cur = INF;
    for (auto a : A) cur = min(cur, dist[a][i]);
    ret += cur;
  }
//  printf("eval: %d, (", A.size());
//  for (auto a : A) printf("%d ",a);
//  printf(") is %lld\n",ret);
  return -ret;
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
  delta = vector <LL>(N, INF);
  cost = vector<LL>(N, 1);
  for (int i=0;i<N;++i) {
    vector <int> edges;
    int K, t;
    fscanf(fin, "%d",&K);
    for (int j=0;j<K;++j) {
      fscanf(fin, "%d",&t);
      edges.push_back(t);
    }
    G.push_back(edges);
  }
  fclose(fin);
}

set<int> lazyForward(bool isUniCost, set<int> init = set<int>()) {
  uniCost = isUniCost;
  set <int, celf_cmp> remaining;
  if (init.size() == 0) {
    for (int i=0;i<N;++i) delta[i] = INF;
    for (int i=0;i<N;++i) remaining.insert(i);
  }
  else {
    for (int i : init) delta[i] = INF;
    for (int i : init) remaining.insert(i);
  }
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
  //  printf("%d\n",cur);
    remainingBudget -= (uniCost) ? 1 : cost[cur];
    ret.insert(cur);
    printf("%lld %.4lf %.4lf\n", budget-remainingBudget, -(LF)eval(ret) / N, (LF)(clock() - start_time) / CLOCKS_PER_SEC);
  }
  return ret;
}

set<int> CELF() {
  preprocess();
  set<int> A = lazyForward(1);
  return A;
  //set<int> B = lazyForward(0);
  //return (eval(A) < eval(B)) ? A : B;
}

int main () {
  start_time = clock();
  //string s;
  //cin >> s;
  //read(s);
  read("input.txt");
  budget = 200;
  set <int> sol = CELF();
}
