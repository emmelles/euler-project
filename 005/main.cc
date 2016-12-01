#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> primeSieve(int);
vector<int> getPrimes(int);

main () {
  int max=10;
  vector<int> collected;
  vector<int> collected2;

  // Wanted to check if a sieve or a straightforward approach is quicker
  clock_t begin = clock();
  collected=primeSieve(max);
  clock_t end = clock();
  double elapsed = double(end - begin) / CLOCKS_PER_SEC;
  cout << "Time elapsed primeSieve " << elapsed << endl;
  
  clock_t begin2 = clock();
  collected2=getPrimes(max);
  clock_t end2 = clock();
  double elapsed2 = double(end2 - begin2) / CLOCKS_PER_SEC;
  cout << "Time elapsed getPrimes  " << elapsed2 << endl;

  vector<int> processed;
  
  for (vector<int>::const_iterator i = collected.begin(); i != collected.end(); ++i) {
    int q=*i;
    int mult=q;
    while (mult <= max/q) {   
      mult*=q;
    }
    processed.push_back(mult);
  }

  int prod=1;
  for (vector<int>::const_iterator i = processed.begin(); i != processed.end(); ++i) {
    int n=*i;
    prod *= n;
  }
  cout << prod <<endl;
}

////////////////////

vector<int> getPrimes(int upto) {
  
  vector<int> dummy;

  for (int n=2; n<=upto; n++) {
    for (int m=2; m<=n; m++) {
      if (m==n) {dummy.push_back(n);}
      if (n % m==0) {break;}
    }
  }
  return dummy;
}

vector<int> primeSieve(int upTo) {

  vector<int> dummy;

  // populate dummy with all numbers up to specified
  for (int n=2; n<=upTo; n++) {
    dummy.push_back(n);
  }

  // remove multiples:
  for (int i=2; i<=upTo/2; i++) {
    for (int j=2; j<=upTo/2; j++) {
      vector<int>:: iterator it = find(dummy.begin(), dummy.end(), j*i);
      if(it != dummy.end()) dummy.erase(it);
    }
  }
    
  return dummy;
}
