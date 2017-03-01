#include <vector>
#include "matrix2D.h"

using namespace std;

template <class Type> Matrix2D<Type>::Matrix2D() {
  m_matrix2D;
  }

template <class Type> Matrix2D<Type>::Matrix2D (long long noOfRows, long long noOfCols) {
  m_matrix2D(noOfRows, vector<Type> (noOfCols,0) );
}

template <class Type> Type Matrix2D<Type>::get(long long n, long long m) {
  return m_matrix2D[n][m];
}

template <class Type> void Matrix2D<Type>::set(long long n, long long m, Type entry) {
  m_matrix2D[n][m]=entry;
}

/*template <class Type> vector<Type> Matrix2D<type>::row(long long n) {
  return m_matrix2D[n];
  }*/
