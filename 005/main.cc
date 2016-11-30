#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> primeSieve(int);

main () {
  int max=20;
  vector<int> collected;
  
  collected=primeSieve(max);
  vector<int> processed;

  for (vector<int>::const_iterator i = collected.begin(); i != collected.end(); ++i) {
    int q=*i;
    int mult=q;
    while (mult <= max/q) {   
      mult*=q;
    }
    processed.push_back(mult);
  }

  int sum=1;
  for (vector<int>::const_iterator i = processed.begin(); i != processed.end(); ++i) {
    int n=*i;
    sum *= n;
  }
  cout << sum <<endl;
}

////////////////////

vector<int> primeSieve(int upto) {
  
  vector<int> dummy;

  for (int n=2; n<=upto; n++) {
    for (int m=2; m<=n; m++) {
      if (m==n) {dummy.push_back(n);}
      if (n % m==0) {break;}
    }
  }
  return dummy;
}
