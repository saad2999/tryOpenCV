create database Tool_Rental;
-- drop database Tool_Rental;
use Tool_Rental;
create table Costumer(
Costumer_id serial primary key,
Fname varchar(10),
Lname varchar(10),
postal_code varchar(20),
phonenumber bigint,
Membership_date date

);

insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
values('peter','parker',10001,01234567,'2008-11-11');
insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
values('Carena','Indgs',164200,	659441,'2022-05-11');

insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
values('Juliet	','santo',05516,	2864210,'2021-11-05');

insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
values('Reinaldo',	'Kleinplatz',	6651,	3189048354,	'2021-12-31');

insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
values('james','rees',164200,	123444,'2012-07-11');

insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
values('Val','Lassetter',761548,	10477521,'2021-10-11');

insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
values('Rodrigo','Piers',86156,	2709345,'2022-07-14');

insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
values('Ardra','Banat',37605,	4236427,'2021-11-12');


select * from Costumer where Costumer_id=1;

create table Tools(
Tool_id serial primary key,
Title varchar(15),
Rental_duration integer
);
insert into Tools(Title,Rental_duration) values('hammer',15);
insert into Tools(Title,Rental_duration) values('Crow bar',10);
insert into Tools(Title,Rental_duration) values('saw',25);
insert into Tools(Title,Rental_duration) values('wrench',35);
insert into Tools(Title,Rental_duration) values('pliers',45);
insert into Tools(Title,Rental_duration) values('Screw driver',5);
insert into Tools(Title,Rental_duration) values('Digital meter',55);
insert into  Tools(Title,Rental_duration) values('snake',65);
select * from Tools;
create table Rentals
(
Rental_id serial primary key,
Rental_date date,
Return_date date,
Costumer_id_Costumers integer ,
Tool_id_Tools integer ,
 FOREIGN KEY (Costumer_id_Costumers) REFERENCES Costumers(Costumer_id),
  FOREIGN KEY (Tool_id_Tools) REFERENCES Tools(Tool_id)

);
insert into Rentals(Rental_date,Return_date,Costumer_id_Costumers,Tool_id_Tools) 
values('2012-07-11','2012-07-18',1,1);
insert into Rentals(Rental_date,Return_date,Costumer_id_Costumers,Tool_id_Tools)
 values('2012-09-10','2012-09-18',2,2);
insert into Rentals(Rental_date,Return_date,Costumer_id_Costumers,Tool_id_Tools)
 values('2014-10-10','2012-10-18',3,3);
insert into Rentals(Rental_date,Return_date,Costumer_id_Costumers,Tool_id_Tools)
 values('2012-09-10','2020-11-12',4,4);
insert into Rentals(Rental_date,Return_date,Costumer_id_Costumers,Tool_id_Tools)
 values('2019-08-11','2019-09-02',5,5);
insert into Rentals(Rental_date,Return_date,Costumer_id_Costumers,Tool_id_Tools)
 values('2018-10-10','2018-09-10',6,6);
insert into Rentals(Rental_date,Return_date,Costumer_id_Costumers,Tool_id_Tools)
 values('2021-09-05','2021-10-05',7,7);
insert into Rentals(Rental_date,Return_date,Costumer_id_Costumers,Tool_id_Tools)
 values('2022-06-31','2022-07-20',8,8);

select* from Rentals;

create table Jobs(
job_id serial primary key,
job_name varchar(20)
);

insert into Jobs(job_name) values('roofing');
insert into Jobs(job_name) values('plumbing');
insert into Jobs(job_name) values('electrical');
select * from Jobs;
create table Tools_jobs(
Tool_jobs_id serial primary key,
job_id_jobs integer ,
Tool_id_tools  integer,

 FOREIGN KEY (job_id_jobs) REFERENCES Jobs(job_id),
  FOREIGN KEY (Tool_id_Tools) REFERENCES Tools(Tool_id)


);


insert into Tools_jobs(job_id_jobs,Tool_id_tools) values(1,1);
insert into  Tools_jobs(job_id_jobs,Tool_id_tools) values(2,1);
insert into Tools_jobs(job_id_jobs,Tool_id_tools) values(3,1);
insert into Tools_jobs(job_id_jobs,Tool_id_tools) values(4,2);
insert into Tools_jobs(job_id_jobs,Tool_id_tools) values(5,2);

insert into Tools_jobs(job_id_jobs,Tool_id_tools) values(6,3);
insert into Tools_jobs(job_id_jobs,Tool_id_tools) values(7,3);
insert into  Tools_jobs(job_id_jobs,Tool_id_tools) values(8,2);
select * from Tools_jobs;