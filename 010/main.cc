#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

template <class Type> void printVector(vector<Type> myVector) {
  for (typename vector<Type>::const_iterator i = myVector.begin(); i != myVector.end(); ++i) {
    cout << *i << "  ";
  }
  cout << endl;
}

vector<long long> getPrimes(long long);

int main () {
  long long max=20;
  vector<long long> collected;

  cout << "collecting primes " << endl;
  collected=getPrimes(max-1); // I mean two million isn't prime but technically this is the question
  
  /*  long long sum=0;
  for (vector<long long>::const_iterator i = collected.begin(); i != collected.end(); ++i) {
    long long n=*i;
    sum += n;
  }
  cout << sum <<endl;*/

  printVector(collected);
}

////////////////////

vector<long long> getPrimes(long long upto) {
  
  vector<long long> dummy;

  cout << "pushing back two" << endl;
  dummy.push_back(2);
  printVector(dummy);

  
  vector<long long>::iterator current_pos=dummy.begin();
    
  for (long long n=3; n<=upto; n++) {
    cout<< "current n " << n << endl;
    cout << "Current highest prime " << *current_pos<< endl;
    for (vector<long long>::const_iterator m=dummy.begin(); m<=current_pos; m++) {
      cout << "# Current m content " << *m <<endl;
      if(*m>sqrt(n)) {
	dummy.push_back(n);
	printVector(dummy);
        advance(current_pos,1);
	break;
      }
      if (n % *m ==0) {break;}
    }
  }
  
  return dummy;
}

