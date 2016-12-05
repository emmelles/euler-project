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
  cout << "Primes up to? [+ve int]\n";
  long long max;
  cin >> max;
  vector<long long> collected;

  cout << "Collecting primes, hang on..." << endl;
  collected=getPrimes(max-1); // I mean two million isn't prime but technically this is the question
  
  long long sum=0;
  for (vector<long long>::const_iterator i = collected.begin(); i != collected.end(); ++i) {
    long long n=*i;
    sum += n;
  }
  cout << "Sum of primes up to " << max << " is " << sum <<endl;

  //printVector(collected);
}

////////////////////

vector<long long> getPrimes(long long upto) {
  
  vector<long long> dummy;

  // Pushing back two
  dummy.push_back(2);

  // Start iterator loop:
  
  vector<long long>::iterator current_pos=dummy.begin();
    
  for (long long n=3; n<=upto; n+=2) {
    for (vector<long long>::const_iterator m = dummy.begin(); m != current_pos+1; m++) {
      if(*m>sqrt(n)) {
	dummy.push_back(n);
        advance(current_pos,1);
	break;
      }
      if (n % *m ==0) {break;}
    }
  }
  
  return dummy;
}

