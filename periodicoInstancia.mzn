var int: lectores;
var int: inter;
var int: nati;
var int: local;
var int: sports;
var int: culture;

var bool: binter;
var bool: bnati;
var bool: blocal;
var bool: bsports;
var bool: bculture;

constraint inter >=5;
constraint inter <=9;
constraint nati >=4;
constraint nati <=7;
constraint local >=2;
constraint local <=5;
constraint sports >=2;
constraint sports <=4;
constraint culture >=1;
constraint culture <=3;

constraint inter*binter + nati*bnati + local*blocal + sports*bsports + culture*bculture <= 10; % limites páginas
%constraint lectores = 1500*inter + 2000*nati + 1000*local + 1500*sports + 750*culture; % lectores
constraint lectores = 1500*inter*binter + 2000*nati*bnati + 1000*local*blocal + 1500*sports*bsports + 750*culture*bculture; % lectores
solve maximize lectores;
