int: n = 5;
array[1..n] of var 1..9: x;
constraint sum(x) = product(x);
constraint forall(i in 1..n-1)(x[i] <= x[i + 1]);
solve maximize product(x);

output["x = array1d(1..5, ", show(x), ");\n"];