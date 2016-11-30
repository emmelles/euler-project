#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

bool checkPalindrome(long long);

int main() {

  long long max=999;

  for (int i=0; i<=(max-100); i++) {
    for (int j=-floor(i/2); j<=0; j++) {

      long long product=(max+j)*(max-j-i);

      if (checkPalindrome(product)) {
	cout << "Largest palindrome is " << product << endl;
	exit (0);
      }
      
    }
  }

}

//======================================================//

bool checkPalindrome(long long number) {

  // See http://stackoverflow.com/questions/4351371/c-performance-challenge-integer-to-stdstring-conversion
  
  stringstream ss;  
  ss<<number;
  string revstring=ss.str();
  string string=revstring;

  reverse(revstring.begin(), revstring.end());
 
  if (revstring.compare(string)==0 ) {
    return true;
  }
  else {
    return false;
  }
  
}
