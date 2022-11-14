var int: utilidad; 
var bool: x1;
var bool: x2;
var bool: x3;
var bool: x4;
var bool: x5;
var bool: x6;

constraint x1*0.2 + x2*2 + x3*2 + x4*0.8+ x5*1 + x6*1 <= 6; % Pesos
constraint utilidad = 12*x1 + 7*x2 + 3*x3 + 4*x4 + 5*x5 + 8*x6; % Utilidades
solve maximize utilidad;
