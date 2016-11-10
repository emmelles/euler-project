#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

bool isMultipleOf(double, int);

main () {

  int limit=4000000;

  int last=1;
  int current=2;

  double sum=2;
  
  while (current<limit) {

    int dummy=last;

    last=current;
    current=current+dummy;

    if (current>limit) break;
    
    cout << current << endl;
    if (isMultipleOf(current,2)) {
      sum=sum+current;
    }
    
  }

  cout << fixed << "The sum of even members is " << sum << endl;
  
}

bool isMultipleOf(double input, int number) {
  double intpart;
  double fracpart = modf(input/number,&intpart);
  if (fracpart==0) { return true;}
  else {return false;}
}
