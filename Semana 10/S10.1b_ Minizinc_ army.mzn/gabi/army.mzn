%Escribir aquí la solución
int: budget = 10000;

var 0..1000: F;
var 0..400: L;
var 0..500: Z;
var 0..150: J;

var int: force;
var int: cost;

% Restricciones de coste
constraint cost = F * 13 + L * 21 + Z * 17 + J * 100;
constraint cost <= budget;

% Fuerza
constraint force = F * 6 + L * 10 + Z * 8 + J * 40;

solve maximize force;

output ["F = ", show(F), ";\nL = ", show(L), ";\nZ = ", show(Z), ";\nJ = ", show(J), ";"]