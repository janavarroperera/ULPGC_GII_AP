include "globals.mzn";

enum Women;
enum Men;

array[Women, Men] of int: wrank;
array[Men, Women] of int: mrank;

%Escribir el código a partir de aquí