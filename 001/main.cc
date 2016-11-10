#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

bool isMultipleOf(double, int);

main () {

  int limit=1000;
  double sum=0;

  for (int i=0; i<limit; i++) {
    if (isMultipleOf(i,5) || isMultipleOf (i,3)) {
      sum=sum+i;
    }
  }

  cout << "Sum of multiples of 3 and 5 up to " << limit
       << " is " << sum << endl;
  
}

bool isMultipleOf(double input, int number) {
  double intpart;
  double fracpart = modf(input/number,&intpart);
  if (fracpart==0) { return true;}
  else {return false;}
}
