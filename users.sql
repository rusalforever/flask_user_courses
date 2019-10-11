DROP DATABASE   IF     EXISTS Users;
CREATE DATABASE IF NOT EXISTS Users;
USE Users;
create table course
(
	id int auto_increment
		primary key,
	name varchar(120) null,
	code varchar(20) not null,
	constraint course_code_uindex
		unique (code)
);

create table user
(
	id int auto_increment
		primary key,
	name varchar(20) not null,
	email varchar(80) not null,
	phone varchar(20) null,
	mobile_phone varchar(20) null,
	status tinyint(1) default 0 null,
	constraint users_name_uindex
		unique (name)
);

create table user_course
(
	user_id int not null,
	course_id int not null,
	constraint course_id
		foreign key (course_id) references course (id)
			on update cascade on delete cascade,
	constraint user_id
		foreign key (user_id) references user (id)
			on update cascade on delete cascade
);

INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (1, 'first user', 'none@none.com', '12345566', '233345', 0);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (7, 'sdavdbsb gghghgg', 'em@em.em', '', '', 1);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (8, 'sdavdbsb gghghggeeee', 'em@em.em', '', '', 1);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (9, 'hggeeee effrff', 'em@em.em', '', '', 1);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (10, 'my name', 'em@em.em', '', '', 1);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (11, 'my name1', 'em@em.em', '', '', 1);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (13, 'my name12', 'em@em.em', '', '', 1);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (15, 'named ffgd', 'some@some.fff', '', '', 1);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (16, 'dg sfewfwre', 'ewwerwre@sdff.dfs', '', '', 0);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (18, 'name3@name3.com', 'name3@name3.com', '', '', 0);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (20, 'name3@name3.com2', 'name3@name3.com', '', '', 0);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (23, 'name3@name', 'name@name.com', '', '', 0);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (24, 'eeeeeee', 'e@email.com', '', '', 0);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (25, 'eeeeee', 'e@email.com', '', '', 0);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (26, 'anme last', '1@1.com', '', '', 0);
INSERT INTO Users.user (id, name, email, phone, mobile_phone, status) VALUES (27, 'wwswsgfghg', 'swsw@sdds.cpm', '', '', 0);

INSERT INTO Users.course (id, name, code) VALUES (1, 'Python', 'jfghhfg');
INSERT INTO Users.course (id, name, code) VALUES (2, 'Flask', 'reghggfh');
INSERT INTO Users.course (id, name, code) VALUES (3, 'Ruby on Rails', '5hhfhfg');
INSERT INTO Users.course (id, name, code) VALUES (4, 'JavaScript', '5trthrth');
INSERT INTO Users.course (id, name, code) VALUES (5, 'HTML', 'h57756jn');
INSERT INTO Users.course (id, name, code) VALUES (6, 'React', 'gh57656');
INSERT INTO Users.course (id, name, code) VALUES (7, 'Angular', 'ghjgjg5756');
INSERT INTO Users.course (id, name, code) VALUES (8, 'Vue', 'gfdhjf');
INSERT INTO Users.course (id, name, code) VALUES (9, 'SQL', 'hjgjgk');

INSERT INTO Users.user_course (user_id, course_id) VALUES (15, 2);
INSERT INTO Users.user_course (user_id, course_id) VALUES (15, 6);
INSERT INTO Users.user_course (user_id, course_id) VALUES (15, 7);
INSERT INTO Users.user_course (user_id, course_id) VALUES (15, 9);
INSERT INTO Users.user_course (user_id, course_id) VALUES (1, 1);
INSERT INTO Users.user_course (user_id, course_id) VALUES (1, 3);