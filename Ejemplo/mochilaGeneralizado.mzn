%Lectura de datos:
int: n;
array[1..n] of float: w;
array[1..n] of float: c;
int: W;

%Variables:
array[1..n] of var bool: x; %  array[1..n] of var 0..1: x; 

%Restricciones:
constraint sum(j in 1..n)( w[j]* x[j] ) <= W;

%Objetivo
var int: utilidad;
constraint utilidad = sum(j in 1..n)( c[j]* x[j] );
solve maximize utilidad;


 