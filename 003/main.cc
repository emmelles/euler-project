#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

main () {

  long long toFactorise=600851475143;
  cout << "Factorising " << toFactorise << endl;
  
  // As it turns out you can use reminder instad of modf, easier.
  long long factor=2;

  // Can optimise vaguely by testing 2, then moving on to dividing
  // only by odds after:

  while ( toFactorise % factor == 0 ) {
    cout << factor << endl;
    toFactorise /= factor;
  }

  factor += 1;
  
  while (factor*factor <= toFactorise) {

    if (toFactorise % factor==0) {
      cout << factor << endl;
      toFactorise=toFactorise/factor;
    }
    else {factor+=2;}

  }

  cout << toFactorise << endl;
  
}

