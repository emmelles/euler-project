#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>

//////////////////////////////////////////////////////////////
// METHOD:
// For this we have A+B+C=N and A*A+B*B=C*C.
// From this get A+B+sqrt(A*A+B*B)-N=0

using namespace std;

int main() {
  long long A;
  long long B;
  long long totSq=1000;

  for (B=1; B<=500; B++) {
    for (A=1; A<=500; A++) {
      double inside=A*A+B*B;
      double root=sqrt(inside);
      double fracpart, intpart;
      fracpart=modf(root,&intpart);
      
      
      if (fracpart==0 && A+B+root==totSq) {
	cout<< "Try " << B << " " << A << " " << totSq-A-B << endl;
	cout << "( product: " << A*B*( totSq-A-B) << " )" << endl;
	exit (0);
      }
    }
  }
  
}
