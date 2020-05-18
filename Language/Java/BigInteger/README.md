# BigIntger Class In Java

-------------------------------------------------------------------------------------------

**BigInteger** class is used for mathematical operation which involves very big integer calculations 
that are outside the limit of all available primitive data types.

There is no theoretical limit on the upper bound of the range because memory is allocated dynamically but practically as memory is limited you can store a number which has Integer.MAX_VALUE number of bits in it which should be sufficient to store mostly all large values.

------------------------------------------------------------------------------------------------------

###### Declaration
```
BigInteger A, B;
```
###### Initialization
```
A  = BigInteger.valueOf(54);
A  = new BigInteger(“54”);
A  = BigInteger.ONE; // Other than this, available constant are BigInteger.ZERO and BigInteger.TEN 
```
###### Mathematical Operations
```
BigInteger C = A.add(B);
BigInteger C = A.subtract(B);
BigInteger C = A.multiply(B);
BigInteger C = A.divide(B);
BigInteger C = A.mod(B); //gives non-negative number
BigInteger C = A.remainder(B);
BigInteger[] D = A.divideAndRemainder(B); // This method returns an array of two BigIntegers containing (this / val) followed by (this % val)
```

###### Comparisons
```
boolean C    = A.equals(B);
BigInteger C = A.max(B);
BigInteger C = A.min(B);
int C        = A.compareTo(B); 
/*
0: if the value of this BigInteger is equal to that of the BigInteger object passed as a parameter.
1: if the value of this BigInteger is greater than that of the BigInteger object passed as a parameter.
-1: if the value of this BigInteger is less than that of the BigInteger object passed as a parameter.
*/
```
###### Conversions
```
double B =  A.doubleValue()
float B  =  A.floatValue()
int B    =  A.intValue()
int B    =  A.longValue()
String B =  A.toString():
String B =  A.toString(int radix)
```

###### Reference
[GeeksForGeeks BigInteger Class](https://www.geeksforgeeks.org/biginteger-class-in-java/)