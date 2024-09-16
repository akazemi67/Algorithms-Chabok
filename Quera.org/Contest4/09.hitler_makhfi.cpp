// Problem's Link: https://quera.org/problemset/158162

#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cstring>

using namespace std;
priority_queue<pair<long,long>, vector<pair<long,long>>, greater<>> pq;
map<int, vector<int>> graph;
char should_add[2000];
long powers[2000];
long results[2000];

void add_to_pq(int u){
    for(auto v : graph[u]){
        if(should_add[v]){
            pq.emplace(powers[v], v);
            should_add[v] = 0;
        }
    }
}

int main(){
    int n, m, u, v;
    cin >> n >> m;
    for(u=1; u<=n; u++)
        cin >> powers[u];
    for(int i=0; i<m; i++){
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    memset(results, 0, sizeof (results));

    for(int start=1; start<=n; start++){
        long curr_pow = powers[start];
        ::memset(should_add, 1, sizeof (should_add));
        should_add[start] = 0;
        add_to_pq(start);

        while(!pq.empty()){
            auto [p,node] = pq.top();
            pq.pop();

            add_to_pq(node);
            if(curr_pow <= p){
                long needed = p - curr_pow + 1;
                results[start] += needed;
                curr_pow += needed;
            }
            curr_pow += p;
        }
    }

    for(u=1; u<=n; u++)
        cout << results[u] << " ";
    return 0;
}

