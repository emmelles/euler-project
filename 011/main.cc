#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>
#include "matrix2D.h"

using namespace std;

int main() {
  /*string filename="input.txt";
  string str;
  unsigned long long takeThisMany;
  cout << "How many consecutive numbers?" <<endl;
  cin >> takeThisMany;*/

  Matrix2D <double> myMat(2,2);

  myMat.set(2,2,3.4);
  double myNum=myMat.get(2,2);

  cout << "myNum "<< myNum << endl;
  
  // Read string in:
  /*ifstream myInput;
  myInput.open(filename.c_str());
  myInput>> str;
  myInput.close();*/

  
  
  /* long long stored_product=1;  
  string snippet;

  // Span the entire string, take a substring of specified length:
  for (unsigned long long n=0; n<=str.length()-takeThisMany; ++n) {

    snippet=str.substr(n,takeThisMany);
    long long product=1;

    // Look inside the substring, skip if contains 0, else multiply:
    for (long long m=0; m<(long long)takeThisMany; ++m) {
    
      if (snippet[m]-'0'==0) {
	break;
      }
      else {
	long long num= snippet[m]-'0'; // handling ASCII
	product *= num;
	} 
      
    }
    
    // Compare product to current highest and store if greater:
    if (product>stored_product) {
      cout << "Current highest snippet: " << snippet << " with a product of "<< product <<endl;
      stored_product=product;
    }
  }
  
  cout << "Max product of " << takeThisMany << " consecutive numbers is " << stored_product << endl;*/
}

  
