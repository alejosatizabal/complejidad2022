%Lectura de datos:
int: t; % Temas
int: p; % Páginas que tiene el periodico
array[1..t] of int: minp; % Cantidad mímima de páginas de un tema
array[1..t] of int: maxp; % Cantidad máxima de páginas de un tema
array[1..t] of int: rea; % Cantidad de lectores promedio

%Variables:
array[1..t] of var int: tp; % Define cuantas hojas se toman de un tema
array[1..t] of var bool: tb; % Define si el tema se escoge o no

%Restricciones:
constraint sum(j in 1..t)( tp[j]* tb[j] ) <= p; % Cantidad de hojas no mayor al límite del periodico

constraint forall ( [ tp[i] <= maxp[i] | i in 1..t] ); % Límite superior de páginas
constraint forall ( [ tp[i] >= minp[i] | i in 1..t] ); % Límite inferior de páginas

%Objetivo
var int: lectores;
constraint lectores = sum(j in 1..t)( rea[j] * tp[j] * tb[j] ); % Lectores
solve maximize lectores;

output ["\nTemas incluidos: ", show(tb)];
output ["\nCantidad de páginas incluidas por tema: ", show(tp)];
output ["\nCantidad de lectores totales: ", show(lectores)];

