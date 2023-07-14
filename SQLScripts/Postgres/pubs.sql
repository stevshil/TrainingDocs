DROP DATABASE IF EXISTS pubs;
CREATE DATABASE pubs;

\c pubs;

CREATE TABLE authors (
   au_id          varchar(11) 	    NOT NULL,
   au_lname       varchar(40)       NOT NULL,
   au_fname       varchar(20)       NOT NULL,
   phone          char(12)          NOT NULL DEFAULT 'UNKNOWN',
   address        varchar(40)           NULL,
   city           varchar(20)           NULL,
   state          char(2)               NULL,
   zip            char(5)               NULL,
   contract       boolean               NOT NULL,
   PRIMARY KEY(au_id)
);

CREATE TABLE publishers (
   pub_id         char(4)           NOT NULL,
   pub_name       varchar(40)           NULL,
   city           varchar(20)           NULL,
   state          char(2)               NULL,
   country        varchar(30)           NULL DEFAULT 'USA',
   PRIMARY KEY(pub_id)
);

CREATE TABLE titles (
   title_id       varchar(6)	    NOT NULL,
   title          varchar(80)       NOT NULL,
   type           char(12)          NOT NULL DEFAULT 'UNDECIDED',
   pub_id         char(4)               NULL,
   price          decimal(4,2)          NULL,
   advance        decimal(10,2)          NULL,
   royalty        int                   NULL,
   ytd_sales      int                   NULL,
   notes          varchar(200)          NULL,
   PRIMARY KEY(title_id)
);


CREATE TABLE titleauthor (
   au_id          varchar(11)	    NOT NULL,
   title_id       varchar(6)	    NOT NULL,	
   au_ord         int               NULL,
   royaltyper     int                   NULL,
   FOREIGN KEY(title_id) REFERENCES titles(title_id),
   PRIMARY KEY(au_id, title_id)
);

CREATE TABLE stores (
   stor_id        char(4)           NOT NULL,
   stor_name      varchar(40)           NULL,
   stor_address   varchar(40)           NULL,
   city           varchar(20)           NULL,
   state          char(2)               NULL,
   zip            char(5)               NULL,
   PRIMARY KEY(stor_id)
);

CREATE TABLE sales (
   stor_id        char(4)           NOT NULL,
   ord_num        varchar(20)       NOT NULL,
   ord_date       char(8)           NOT NULL,
   qty            smallint          NOT NULL,
   payterms       varchar(12)       NOT NULL,
   title_id       varchar(6)	    NOT NULL,
   FOREIGN KEY(title_id) REFERENCES titles(title_id),
   FOREIGN KEY(stor_id) REFERENCES stores(stor_id),
   PRIMARY KEY(stor_id, ord_num, title_id)
);

CREATE TABLE roysched (
   title_id       varchar(6)	    NOT NULL,
   lorange        int                   NULL,
   hirange        int                   NULL,
   royalty        int                   NULL,
   FOREIGN KEY(title_id) REFERENCES titles(title_id)
);

CREATE TABLE discounts (
   discounttype   varchar(40)       NOT NULL,
   stor_id        char(4) 		NULL,
   lowqty         smallint              NULL,
   highqty        smallint              NULL,
   discount       dec(4,2)          NOT NULL,
   FOREIGN KEY(stor_id) REFERENCES stores(stor_id)
);

CREATE TABLE jobs (
   job_id         SERIAL          NOT NULL,
   job_desc       varchar(50)       NOT NULL DEFAULT 'New Position - title not formalized yet',
   min_lvl        int           NOT NULL,
   max_lvl        int           NOT NULL,
   PRIMARY KEY(job_id)
);


CREATE TABLE employee (
   emp_id         char(9)     	    NOT NULL,
   fname          varchar(20)       NOT NULL,
   minit          char(1)               NULL,
   lname          varchar(30)       NOT NULL,
   job_id         int          NOT NULL DEFAULT '1',
   job_lvl        int	    		NOT NULL DEFAULT '10',
   pub_id         char(4)           NOT NULL DEFAULT '9952',
   hire_date      char(8)           NOT NULL DEFAULT '19950818',
   PRIMARY KEY(emp_id),
   FOREIGN KEY(job_id) REFERENCES jobs(job_id),
   FOREIGN KEY(pub_id) REFERENCES publishers(pub_id)
);


insert into authors
   values('409-56-7008', 'Bennet', 'Abraham', '415 658-9932',
   '6223 Bateman St.', 'Berkeley', 'CA', '94705', True);
insert into authors
   values('213-46-8915', 'Green', 'Marjorie', '415 986-7020',
   '309 63rd St. #411', 'Oakland', 'CA', '94618', True);
insert into authors
   values('238-95-7766', 'Carson', 'Cheryl', '415 548-7723',
   '589 Darwin Ln.', 'Berkeley', 'CA', '94705', True);
insert into authors
   values('998-72-3567', 'Ringer', 'Albert', '801 826-0752',
   '67 Seventh Av.', 'Salt Lake City', 'UT', '84152', True);
insert into authors
   values('899-46-2035', 'Ringer', 'Anne', '801 826-0752',
   '67 Seventh Av.', 'Salt Lake City', 'UT', '84152', True);
insert into authors
   values('722-51-5454', 'DeFrance', 'Michel', '219 547-9982',
   '3 Balding Pl.', 'Gary', 'IN', '46403', True);
insert into authors
   values('807-91-6654', 'Panteley', 'Sylvia', '301 946-8853',
   '1956 Arlington Pl.', 'Rockville', 'MD', '20853', True);
insert into authors
   values('893-72-1158', 'McBadden', 'Heather',
   '707 448-4982', '301 Putnam', 'Vacaville', 'CA', '95688', False);
insert into authors
   values('724-08-9931', 'Stringer', 'Dirk', '415 843-2991',
   '5420 Telegraph Av.', 'Oakland', 'CA', '94609', False);
insert into authors
   values('274-80-9391', 'Straight', 'Dean', '415 834-2919',
   '5420 College Av.', 'Oakland', 'CA', '94609', True);
insert into authors
   values('756-30-7391', 'Karsen', 'Livia', '415 534-9219',
   '5720 McAuley St.', 'Oakland', 'CA', '94609', True);
insert into authors
   values('724-80-9391', 'MacFeather', 'Stearns', '415 354-7128',
   '44 Upland Hts.', 'Oakland', 'CA', '94612', True);
insert into authors
   values('427-17-2319', 'Dull', 'Ann', '415 836-7128',
   '3410 Blonde St.', 'Palo Alto', 'CA', '94301', True);
insert into authors
   values('672-71-3249', 'Yokomoto', 'Akiko', '415 935-4228',
   '3 Silver Ct.', 'Walnut Creek', 'CA', '94595', True);
insert into authors
   values('267-41-2394', 'O''Leary', 'Michael', '408 286-2428',
   '22 Cleveland Av. #14', 'San Jose', 'CA', '95128', True);
insert into authors
   values('472-27-2349', 'Gringlesby', 'Burt', '707 938-6445',
   'PO Box 792', 'Covelo', 'CA', '95428', True);
insert into authors
   values('527-72-3246', 'Greene', 'Morningstar', '615 297-2723',
   '22 Graybar House Rd.', 'Nashville', 'TN', '37215', False);
insert into authors
   values('172-32-1176', 'White', 'Johnson', '408 496-7223',
   '10932 Bigge Rd.', 'Menlo Park', 'CA', '94025', True);
insert into authors
   values('712-45-1867', 'del Castillo', 'Innes', '615 996-8275',
   '2286 Cram Pl. #86', 'Ann Arbor', 'MI', '48105', True);
insert into authors
   values('846-92-7186', 'Hunter', 'Sheryl', '415 836-7128',
   '3410 Blonde St.', 'Palo Alto', 'CA', '94301', True);
insert into authors
   values('486-29-1786', 'Locksley', 'Charlene', '415 585-4620',
   '18 Broadway Av.', 'San Francisco', 'CA', '94130', True);
insert into authors
   values('648-92-1872', 'Blotchet-Halls', 'Reginald', '503 745-6402',
   '55 Hillsdale Bl.', 'Corvallis', 'OR', '97330', True);
insert into authors
   values('341-22-1782', 'Smith', 'Meander', '913 843-0462',
   '10 Mississippi Dr.', 'Lawrence', 'KS', '66044', False);


insert into publishers values('0736', 'New Moon Books', 'Boston', 'MA', 'USA');
insert into publishers values('0877', 'Binnet & Hardley', 'Washington', 'DC', 'USA');
insert into publishers values('1389', 'Algodata Infosystems', 'Berkeley', 'CA', 'USA');
insert into publishers values('9952', 'Scootney Books', 'New York', 'NY', 'USA');
insert into publishers values('1622', 'Five Lakes Publishing', 'Chicago', 'IL', 'USA');
insert into publishers values('1756', 'Ramona Publishers', 'Dallas', 'TX', 'USA');
insert into publishers values('9901', 'GGG&G', 'Munchen', NULL, 'Germany');
insert into publishers values('9999', 'Lucerne Publishing', 'Paris', NULL, 'France');


insert into titles values ('PC8888', 'Secrets of Silicon Valley', 'popular_comp', '1389', 20.00, 8000.00, 10, 4095, 'Muckraking reporting on the world''s largest computer hardware and software manufacturers.');
insert into titles values ('BU1032', 'The Busy Executive''s Database Guide', 'business', '1389', 19.99, 5000.00, 10, 4095, 'An overview of available database systems with emphasis on common business applications. Illustrated.');
insert into titles values ('PS7777', 'Emotional Security: A New Algorithm', 'psychology', '0736', 7.99, 4000.00, 10, 3336, 'Protecting yourself and your loved ones from undue emotional stress in the modern world. Use of computer and nutritional aids emphasized.');
insert into titles values ('PS3333', 'Prolonged Data Deprivation: Four Case Studies', 'psychology', '0736', 19.99, 2000.00, 10, 4072, 'What happens when the data runs dry?  Searching evaluations of information-shortage effects.');
insert into titles values ('BU1111', 'Cooking with Computers: Surreptitious Balance Sheets', 'business', '1389', 11.95, 5000.00, 10, 3876, 'Helpful hints on how to use your electronic resources to the best advantage.');
insert into titles values ('MC2222', 'Silicon Valley Gastronomic Treats', 'mod_cook', '0877', 19.99, 0.00, 12, 2032, 'Favorite recipes for quick, easy, and elegant meals.');
insert into titles values ('TC7777', 'Sushi, Anyone?', 'trad_cook', '0877', 14.99, 8000.00, 10, 4095, 'Detailed instructions on how to make authentic Japanese sushi in your spare time.');
insert into titles values ('TC4203', 'Fifty Years in Buckingham Palace Kitchens', 'trad_cook', '0877', 11.95, 4000.00, 14, 15096, 'More anecdotes from the Queen''s favorite cook describing life among English royalty. Recipes, techniques, tender vignettes.');
insert into titles values ('PC1035', 'But Is It User Friendly?', 'popular_comp', '1389', 22.95, 7000.00, 16, 8780, 'A survey of software for the naive user, focusing on the ''friendliness'' of each.');
insert into titles values('BU2075', 'You Can Combat Computer Stress!', 'business', '0736',2.99, 10125.00, 24, 18722,'The latest medical and psychological techniques for living with the electronic office. Easy-to-understand explanations.');
insert into titles values('PS2091', 'Is Anger the Enemy?', 'psychology', '0736', 10.95,2275.00, 12, 2045,'Carefully researched study of the effects of strong emotions on the body. Metabolic charts included.');
insert into titles values('PS2106', 'Life Without Fear', 'psychology', '0736', 7.00, 6000.00,10, 111,'New exercise, meditation, and nutritional techniques that can reduce the shock of daily interactions. Popular audience. Sample menus included, exercise video available separately.');
insert into titles values('MC3021', 'The Gourmet Microwave', 'mod_cook', '0877', 2.99,15000.00, 24, 22246,'Traditional French gourmet recipes adapted for modern microwave cooking.');
insert into titles values('TC3218', 'Onions, Leeks, and Garlic: Cooking Secrets of the Mediterranean','trad_cook', '0877', 20.95, 7000.00, 10, 375,'Profusely illustrated in color, this makes a wonderful gift book for a cuisine-oriented friend.');
insert into titles values ('BU7832', 'Straight Talk About Computers', 'business', '1389',19.99, 5000.00, 10, 4095,'Annotated analysis of what computers can do for you: a no-hype guide for the critical user.');
insert into titles values('PS1372', 'Computer Phobic AND Non-Phobic Individuals: Behavior Variations','psychology', '0877', 21.59, 7000.00, 10, 375,'A must for the specialist, this book examines the difference between those who hate and fear computers and those who don''t.');


insert into titleauthor values('409-56-7008', 'BU1032', 1, 60);
-- insert into titleauthor values('486-29-1786', 'PC9999', 1, 100);
insert into titleauthor values('712-45-1867', 'MC2222', 1, 100);
insert into titleauthor values('172-32-1176', 'PS3333', 1, 100);
insert into titleauthor values('238-95-7766', 'PC1035', 1, 100);
insert into titleauthor values('213-46-8915', 'BU2075', 1, 100);
insert into titleauthor values('998-72-3567', 'PS2091', 1, 50);
insert into titleauthor values('722-51-5454', 'MC3021', 1, 75);
insert into titleauthor values('899-46-2035', 'MC3021', 2, 25);
insert into titleauthor values('807-91-6654', 'TC3218', 1, 100);
insert into titleauthor values('274-80-9391', 'BU7832', 1, 100);
insert into titleauthor values('427-17-2319', 'PC8888', 1, 50);
insert into titleauthor values('846-92-7186', 'PC8888', 2, 50);
insert into titleauthor values('756-30-7391', 'PS1372', 1, 75);
insert into titleauthor values('724-80-9391', 'PS1372', 2, 25);
insert into titleauthor values('267-41-2394', 'BU1111', 2, 40);
insert into titleauthor values('672-71-3249', 'TC7777', 1, 40);
insert into titleauthor values('267-41-2394', 'TC7777', 2, 30);
insert into titleauthor values('472-27-2349', 'TC7777', 3, 30);
insert into titleauthor values('648-92-1872', 'TC4203', 1, 100);


insert into stores values('7066','Barnum''s','567 Pasadena Ave.','Tustin','CA','92789');
insert into stores values('7067','News & Brews','577 First St.','Los Gatos','CA','96745');
insert into stores values('7131','Doc-U-Mat: Quality Laundry and Books',
      '24-A Avogadro Way','Remulade','WA','98014');
insert into stores values('8042','Bookbeat','679 Carson St.','Portland','OR','89076');
insert into stores values('6380','Eric the Read Books','788 Catamaugus Ave.',
      'Seattle','WA','98056');
insert into stores values('7896','Fricative Bookshop','89 Madison St.','Fremont','CA','90019');


insert into sales values('7066', 'QA7442.3', '19940913', 75, 'ON invoice','PS2091');
insert into sales values('7067', 'D4482', '19940914', 10, 'Net 60','PS2091');
insert into sales values('7131', 'N914008', '19940914', 20, 'Net 30','PS2091');
insert into sales values('8042', '423LL922', '19940914', 15, 'ON invoice','MC3021');
insert into sales values('6380', '722a', '19940913', 3, 'Net 60','PS2091');
insert into sales values('8042','P723', '19930311', 25, 'Net 30', 'BU1111');
insert into sales values('7896','QQ2299', '19931028', 15, 'Net 60', 'BU7832');
insert into sales values('7066','A2976', '19930524', 50, 'Net 30', 'PC8888');
insert into sales values('7131','P3087a', '19930529', 25, 'Net 60', 'PS7777');
insert into sales values('7067','P2121', '19920615', 40, 'Net 30', 'TC3218');

insert into roysched values('BU1032', 0, 5000, 10);
insert into roysched values('PC1035', 10001, 50000, 18);
insert into roysched values('BU2075', 0, 1000, 10);
insert into roysched values('PS2091', 1001, 5000, 12);
insert into roysched values('PS2106', 5001, 10000, 14);
insert into roysched values('MC3021', 10001, 12000, 22);
insert into roysched values('TC3218', 14001, 50000, 24);
insert into roysched values('PC8888', 0, 5000, 10);
insert into roysched values('PS7777', 0, 5000, 10);
insert into roysched values('PS3333', 15001, 50000, 16);
insert into roysched values('BU1111', 8001, 10000, 14);
insert into roysched values('PS1372', 40001, 50000, 18);


insert into discounts values('Initial Customer', NULL, NULL, NULL, 10.5);
insert into discounts values('Volume Discount', NULL, 100, 1000, 6.7);
insert into discounts values('Customer Discount', '8042', NULL, NULL, 5.0);


insert into jobs(job_desc, min_lvl, max_lvl) values ('New Hire - Job not specified', 10, 10);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Chief Executive Officer', 200, 250);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Business Operations Manager', 175, 225);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Chief Financial Officier', 175, 250);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Publisher', 150, 250);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Managing Editor', 140, 225);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Marketing Manager', 120, 200);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Public Relations Manager', 100, 175);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Acquisitions Manager', 75, 175);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Productions Manager', 75, 165);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Operations Manager', 75, 150);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Editor', 25, 100);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Sales Representative', 25, 100);
insert into jobs(job_desc, min_lvl, max_lvl) values ('Designer', 25, 100);


insert into employee values ('PTC11962M', 'Philip', 'T', 'Cramer', 2, 215, '9952', '19891111');
insert into employee values ('AMD15433F', 'Ann', 'M', 'Devon', 3, 200, '9952', '19910716');
insert into employee values ('F-C16315M', 'Francisco', '', 'Chang', 4, 227, '9952', '19901103');
insert into employee values ('LAL21447M', 'Laurence', 'A', 'Lebihan', 5, 175, '0736', '19900603');
insert into employee values ('PXH22250M', 'Paul', 'X', 'Henriot', 5, 159, '0877', '19930819');
insert into employee values ('SKO22412M', 'Sven', 'K', 'Ottlieb', 5, 150, '1389', '19910405');
insert into employee values ('RBM23061F', 'Rita', 'B', 'Muller', 5, 198, '1622', '19931009');
insert into employee values ('MJP25939M', 'Maria', 'J', 'Pontes', 5, 246, '1756', '19890301');
insert into employee values ('JYL26161F', 'Janine', 'Y', 'Labrune', 5, 172, '9901', '19910526');
insert into employee values ('CFH28514M', 'Carlos', 'F', 'Hernadez', 5, 211, '9999', '19890421');
insert into employee values ('VPA30890F', 'Victoria', 'P', 'Ashworth', 6, 140, '0877', '19900913');
insert into employee values ('L-B31947F', 'Lesley', '', 'Brown', 7, 120, '0877', '19910213');
insert into employee values ('ARD36773F', 'Anabela', 'R', 'Domingues', 8, 100, '0877', '19930127');
insert into employee values ('M-R38834F', 'Martine', '', 'Rance', 9, 75, '0877', '19920205');
insert into employee values ('PHF38899M', 'Peter', 'H', 'Franken', 10, 75, '0877', '19920517');
insert into employee values ('DBT39435M', 'Daniel', 'B', 'Tonini', 11, 75, '0877', '19900101');
insert into employee values ('H-B39728F', 'Helen', '', 'Bennett', 12, 35, '0877', '19890921');
insert into employee values ('PMA42628M', 'Paolo', 'M', 'Accorti', 13, 35, '0877', '19920827');
insert into employee values ('ENL44273F', 'Elizabeth', 'N', 'Lincoln', 14, 35, '0877', '19900724');
insert into employee values ('MGK44605M', 'Matti', 'G', 'Karttunen', 6, 220, '0736', '19940501');
insert into employee values ('PDI47470M', 'Palle', 'D', 'Ibsen', 7, 195, '0736', '19930509');
insert into employee values ('MMS49649F', 'Mary', 'M', 'Saveley', 8, 175, '0736', '19930629');
insert into employee values ('GHT50241M', 'Gary', 'H', 'Thomas', 9, 170, '0736', '19880809');
insert into employee values ('MFS52347M', 'Martin', 'F', 'Sommer', 10, 165, '0736', '19900413');
insert into employee values ('R-M53550M', 'Roland', '', 'Mendel', 11, 150, '0736', '19910905');
insert into employee values ('HAS54740M', 'Howard', 'A', 'Snyder', 12, 100, '0736', '19881119');
insert into employee values ('TPO55093M', 'Timothy', 'P', 'O''Rourke', 13, 100, '0736', '19880619');
insert into employee values ('KFJ64308F', 'Karin', 'F', 'Josephs', 14, 100, '0736', '19921017');
insert into employee values ('DWR65030M', 'Diego', 'W', 'Roel', 6, 192, '1389', '19911216');
insert into employee values ('M-L67958F', 'Maria', '', 'Larsson', 7, 135, '1389', '19920327');
insert into employee values ('PSP68661F', 'Paula', 'S', 'Parente', 8, 125, '1389', '19940119');
insert into employee values ('MAS70474F', 'Margaret', 'A', 'Smith', 9, 78, '1389', '19880929');
insert into employee values ('A-C71970F', 'Aria', '', 'Cruz', 10, 87, '1389', '19911026');
insert into employee values ('MAP77183M', 'Miguel', 'A', 'Paolino', 11, 112, '1389', '19921207');
insert into employee values ('Y-L77953M', 'Yoshi', '', 'Latimer', 12, 32, '1389', '19890611');
insert into employee values ('CGS88322F', 'Carine', 'G', 'Schmitt', 13, 64, '1389', '19920707');
insert into employee values ('PSA89086M', 'Pedro', 'S', 'Afonso', 14, 89, '1389', '19901224');
insert into employee values ('A-R89858F', 'Annette', '', 'Roulet', 6, 152, '9999', '19900221');
insert into employee values ('HAN90777M', 'Helvetius', 'A', 'Nagy', 7, 120, '9999', '19930319');
insert into employee values ('M-P91209M', 'Manuel', '', 'Pereira', 8, 101, '9999', '19890109');
insert into employee values ('KJJ92907F', 'Karla', 'J', 'Jablonski', 9, 170, '9999', '19940311');
insert into employee values ('POK93028M', 'Pirkko', 'O', 'Koskitalo', 10, 80, '9999', '19931129');
insert into employee values ('PCM98509F', 'Patricia', 'C', 'McKenna', 11, 150, '9999', '19890801');