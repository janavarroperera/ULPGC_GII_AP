int: n= 5;

%Introduzca el código a partir de esta línea
array[1..n] of var 0..3: lista;

constraint lista[1] == 0;
constraint lista[n] == 3;

constraint forall(i in 1..n-1)(lista[i] + lista[i+1] <= 3);
constraint forall(i in 1..n)(i mod 3 == 0 -> lista[i] >= 2);

solve maximize sum(lista);

output ["x = ", show(lista)];