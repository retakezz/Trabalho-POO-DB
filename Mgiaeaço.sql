create database if not exists magiaeaço_db;
use magiaeaço_db;

create table if not exists personagens (
id INT AUTO_INCREMENT PRIMARY KEY,
nome varchar(11) NOT NULL UNIQUE, 
defesa varchar(21) not null, 
arma varchar(19),
elemento varchar(6),
vida int not null,
ataque varchar(19) not null,
classe enum("Mago" , "Cavaleiro") 
) ; 