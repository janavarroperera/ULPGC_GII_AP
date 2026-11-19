%Escribir solución aquí
include "globals.mzn";

var int: army;

constraint army > 100;
constraint army < 500;

constraint army mod 5 = 2;
constraint army mod 7 = 2;
constraint army mod 12 = 1;

output ["army = ", show(army)];