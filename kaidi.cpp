#include <iostream>
#include <set>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <fstream>

#define INF 100000000

using namespace std;

// global variable meh who cares
int totalNodes;
vector<vector<int> > dist;
vector<vector<int> > edges;

double evaluation(const set<int>& setOfNodes){
  double result = 0;
  for (int i = 0; i < totalNodes; i++) {
    int minResult = INF;
    for (auto s: setOfNodes) {
      minResult = min(minResult, dist[i][s]);
    }

    result += minResult;
  }
  return -result / totalNodes;
}

set<int> remain(int budget, const vector<int>& costs,
    const set<int>& result) {

  int totalCost = 0;
  set<int> remaining;
  for (auto r : result) totalCost += costs[r];
  for (int i = 0; i < totalNodes; i++) {
    if (result.find(i) != result.end()) continue;
    if (costs[i] + totalCost <= budget) remaining.insert(i);
  }
  return remaining;
}

set<int> lazyForward(int budget, const vector<int>& costs, int type) {
  set<int> result;
  set<int> remaining;
  vector<double> delta(totalNodes, INF);

  remaining = remain(budget, costs, result);
  while (!remaining.empty()) {
    vector<bool> cur(totalNodes, false);
    while (true) {
      int sBest = 0;
      double bestValue = -1000000;
      if (type == 0) {
        for (auto s : remaining) {
          if (delta[s] > bestValue) {
            bestValue = delta[s];
            sBest = s;
          }
        }
      } else {
        for (auto s : remaining) {
          if (delta[s] / costs[s] > bestValue) {
            bestValue = delta[s] / costs[s];
            sBest = s;
          }
        }
      }
      if (cur[sBest]) {
        result.insert(sBest);
        remaining = remain(budget, costs, result);
        cout << "found one ... " << sBest << endl;
        break;
      } else {
        cur[sBest] = true;
        set<int> temp = result;
        temp.insert(sBest);
        delta[sBest] = evaluation(temp) - evaluation(result);
      }
    }
  }
  return result;
}


set<int> CELF(int budget, const vector<int>& costs) {
  set<int> ucResult = lazyForward(budget, costs, 0);
  return ucResult;

  set<int> cbResult = lazyForward(budget, costs, 1);
  if (evaluation(ucResult) > evaluation(cbResult))
    return ucResult;
  else
    return cbResult;
}

void bfs(int start, vector<int>& distances) {
  unordered_set<int> visited;
  visited.insert(start);
  distances[start] = 0;
  queue<pair<int, int> > q;
  q.push(make_pair(start, 0));

  while (!q.empty()) {
    int curr = q.front().first;
    int distance = q.front().second;
    q.pop();
    for (auto x: edges[curr]) {
      if (visited.find(x) == visited.end()) {
        visited.insert(x);
        distances[x] = distance + 1;
        q.push(make_pair(x, distance + 1));
      }
    }
  }
}

void preprocess() {
  for (int i = 0; i < totalNodes; i++) {
    vector<int> distances(totalNodes, INF);
    bfs(i, distances);
    dist.push_back(distances);
  }
}

int main() {
  ifstream fin("input.txt");
  fin >> totalNodes;
  for (int i = 0; i < totalNodes; i++) {
    vector<int> edge;
    int degrees;
    fin >> degrees;
    for (int j = 0; j < degrees; j++) {
      int x;
      fin >> x;
      edge.push_back(x);
    }
    edges.push_back(edge);
  }
  preprocess();

  int budget;
  cin >> budget;
  vector<int> costs(totalNodes, 1);
  set<int> result = CELF(budget, costs);
  for (auto s: result) cout << s << endl;
  cout << evaluation(result) << endl;

  ofstream fout("output.txt");
  for (int i = 0; i < totalNodes; i++) {
    for (int j = 0; j < totalNodes; j++) 
      fout << dist[i][j] << " ";
    fout << endl;
  }
  return 0;
}
