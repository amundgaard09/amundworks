
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 9x9 grid
vector<vector<char>> grid(9, vector<char>(9, '.'));

void Update(vector<vector<char>>& grid) {
     //placeholder for tick update
}

void PrintGrid(vector<vector<char>>& grid){
    for (int row = 0; row < grid.size(); row++) {
        for (int col = 0; col < grid[row].size(); col++) {
            cout << grid[row][col];
        }
        cout << "\n";
    }
}

int main() {
    PrintGrid(grid);
    return 0;
}