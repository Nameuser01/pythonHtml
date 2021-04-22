drop table if exists util;
drop table if exists contact;
/* Création des tables */
create table util(
	id_util serial primary key,
	login varchar(20),
	mdp varchar(20)
);

create table contact(
	id_contact serial primary key,
	nom varchar(100),
	email varchar(100),
	tel varchar(10),
	adresse varchar(100), 
	id_util int,
	foreign key(id_util) references util
);

/* Remplissage de tables */

insert into util(login, mdp) values(
	'root',
	'123456'
);/*Comme root est le premier utilisateur a être créé, son id 
vaut 1, on respecte donc la consigne*/
insert into util(login, mdp) values(
	'user',
	'123456'
);

insert into contact(nom, email, tel, adresse, id_util) values(
	'George Boole',
	'G.boole@gmx.com',
	'0651628495',
	'01 rue du chat',
	1
);
insert into contact(nom, email, tel, adresse, id_util) values(
	'Grace Hopper',
	'G.hopper',
	'0653546298',
	'10 rue du chat',
	1
);