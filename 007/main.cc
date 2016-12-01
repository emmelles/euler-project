#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <ctime>

using namespace std;

vector<long long> keepNPrimes(long long);

// Playing around with templating and overloading, not necessary:

template <class Type> void printVector(vector<Type> myVector) {
  for (typename vector<Type>::const_iterator i = myVector.begin(); i != myVector.end(); ++i) {
    cout << *i << "  ";
  }
  cout << endl;
}

template <class Type> void myprint(string qualifier, Type stuff) {
  cout << qualifier << stuff << endl;
}

template <class Type> void myprint(Type stuff) {
  cout << stuff << endl;
}

////////////////////

main () {

  long long howManyPrimes;
  myprint("How many primes?");
  cin >> howManyPrimes;
  vector<long long> collected;

  collected=keepNPrimes(howManyPrimes);

  vector<long long>::iterator i=collected.end()-1;
  cout << "Prime number " << howManyPrimes <<" is "<<*i<<endl;

}

////////////////////

vector<long long> keepNPrimes(long long soManyPrimes) {

  double upto=2e+63;
  vector<long long> dummy;
  long long counter=0;

  for (long long n=2; n<=upto && counter < soManyPrimes; n++) {
    for (long long m=2; m<=n; m++) {
      if (m==n) {
	dummy.push_back(n);
	counter++;}
      if (n % m==0) {break;}
    }
  }
  
  return dummy;
}

