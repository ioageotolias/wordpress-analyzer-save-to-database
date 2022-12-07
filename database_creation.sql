create schema websites;
use websites;
create table w_list (
	id int AUTO_INCREMENT primary key,
    name varchar(100),
    analytics varchar(3),
    theme varchar(100));

create table scripts (
	w_id int,
    w_script MEDIUMTEXT,
    foreign key (w_id) references w_list(id));
    
create table plugins (
	w_id int,
    w_plugin varchar(100),
    foreign key (w_id) references w_list(id));
create table nowp (
	nw_id int AUTO_INCREMENT primary key not null,
    nw_list varchar(100) DEFAULT '' not null);