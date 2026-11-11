  include "globals.mzn";
  int: n;
  array[1..n] of var 0..9: x;
  
  constraint sum(x) == product(x);
  constraint increasing(x);

  
  solve maximize sum(x);
