class Solution {
public:
    
  long getQuotient(int div, int divis) {
    long q;
        
    long dividend = labs(div);
    long divisor = labs(divis);
        
    if(dividend < divisor) {
      return 0;
    }
        
    int sign = 1;
        
    long l = 1;
    long h = dividend;
        
    while(l < h) {
      q = l + (h-l)/2;
      if(divisor * q == dividend) {
	return q;
      } else if (divisor * q <= dividend) {
	if(divisor * (q+1) > dividend) {
	  return q;
	}
	l = q + 1;
      } else {
	h = q - 1;
      }
    }
                
    q = l + (h-l)/2;
                
    return q;
  }
    
  int divide(int dividend, int divisor) {        
    if(!divisor  || (dividend == INT_MIN && divisor == -1)) {
      return INT_MAX;
    }
        
    int sign = 1;
        
    if (dividend > 0 && divisor < 0 || dividend < 0 && divisor > 0) {
      sign = -1;
    }
                
                
    try {
      int q = sign * getQuotient(dividend, divisor);
      return q;
    } catch(overflow_error & e) {
      cout << "here!" << endl;
      return INT_MAX;
    }
  }
};
