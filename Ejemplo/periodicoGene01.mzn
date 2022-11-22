%Lectura de datos:
%int: n; % DE MOCHILA
%array[1..n] of float: w; % DE MOCHILA
%array[1..n] of float: c; % DE MOCHILA
%int: W; % DE MOCHILA

int: t; % Temas
int: p; % Páginas que tiene el periodico
array[1..t] of int: minp; % Cantidad mímima de páginas de un tema
array[1..t] of int: maxp; % Cantidad máxima de páginas de un tema
array[1..t] of int: rea; % Cantidad de lectores promedio

%Variables:
%array[1..n] of var bool: x; %  array[1..n] of var 0..1: x; % DE MOCHILA

array[1..t] of var int: tp; % Define cuantas hojas se toman de un tema
array[1..t] of var bool: tb; % Define si el tema se escoge o no

%Restricciones:
%constraint sum(j in 1..n)( w[j]* x[j] ) <= W; % DE MOCHILA

constraint sum(j in 1..t)( tp[j]* tb[j] ) <= p; % Cantidad de hojas no mayor al límite del periodico

%constraint forall ( [ a[i] != a[j] | i, j in 1..3 where i < j ] );
constraint forall ( [ tp[i] <= maxp[i] | i in 1..t] ); % Límite superior de páginas
constraint forall ( [ tp[i] >= minp[i] | i in 1..t] ); % Límite inferior de páginas

%constraint inter >=5;
%constraint inter <=9;
%constraint nati >=4;
%constraint nati <=7;
%constraint local >=2;
%constraint local <=5;
%constraint sports >=2;
%constraint sports <=4;
%constraint culture >=1;
%constraint culture <=3;

%constraint inter*binter + nati*bnati + local*blocal + sports*bsports + culture*bculture <= 10; % limites páginas
%constraint lectores = 1500*inter + 2000*nati + 1000*local + 1500*sports + 750*culture; % lectores
%constraint lectores = 1500*inter*binter + 2000*nati*bnati + 1000*local*blocal + 1500*sports*bsports + 750*culture*bculture; % lectores

%Objetivo
%var int: utilidad; % DE MOCHILA
%constraint utilidad = sum(j in 1..n)( c[j]* x[j] ); % DE MOCHILA
%solve maximize utilidad; % DE MOCHILA

var int: lectores;
%constraint lectores = 1500*inter*binter + 2000*nati*bnati + 1000*local*blocal + 1500*sports*bsports + 750*culture*bculture; % lectores
constraint lectores = sum(j in 1..t)( rea[j] * tp[j] * tb[j] ); % Lectores
solve maximize lectores;

%------------------------------

