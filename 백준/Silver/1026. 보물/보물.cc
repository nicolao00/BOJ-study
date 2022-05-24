#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int i, int j)
{
    if (i > j) return true;
    else return false;
}

int main()
{
    int a[50], b[50], temp[50];
    int bSort[50] = {0, };
    int size = 0, idx = 0;

    cin >> size;
    for (int i = 0; i < size; i++)
        cin >> a[i];
    for (int i = 0; i < size; i++)
        cin >> b[i];
    copy(a, a + size, temp);
    sort(temp, temp + size, compare);
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if (b[i] > b[j])
                bSort[i]++;
            if (b[i] == b[j] && i > j)
                bSort[i]++;
        }
    }
    for (int i = 0; i < size; i++)
        a[i] = temp[bSort[i]];
    int result = 0;
    for (int i = 0; i < size; i++)
        result += a[i] * b[i];
    cout << result;
}