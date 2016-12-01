#include <cstdlib>
#include <iostream>

using namespace std;

main() {
  int max=100;
  int Sum=0;
  int sumOfSquares=0;
  for (int n=0; n<=max; n++) {
    sumOfSquares+=(n*n);
    Sum+=n;
  }

  int res=-sumOfSquares+Sum*Sum;

  cout << res << endl;
  
}
