#ifndef MATRIX2D_H
#define MATRIX2D_H

#include <vector>

using namespace std;

template <class Type> class Matrix2D {
public:
  Matrix2D();
  Matrix2D(long long noOfRows,long long noOfCols);
  Type get(long long n, long long m);
  void set(long long n, long long m, Type entry);

  /*
  vector<Type> row(long long n);
  void setRow(vector<Type> row);

  vector<Type> col(long long n);
  void setCol(vector<Type> col);

  // return the diagonal the entry is in
  // either Top Right to Bottom Left
  vector<Type> antidiag(long long n, long long m);
  // or Top Left to Bottom
  vector<Type> diag(long long n, long long m);*/
  
private:
  vector< vector<Type> > m_matrix2D;
};
  
#endif
