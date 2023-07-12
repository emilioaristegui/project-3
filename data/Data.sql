--drop table merged;

CREATE TABLE merged (
    region varchar(30) NOT NULL,
    Country varchar(30) NOT NULL,
	emissions float NOT NULL,
	industry varchar(30) NOT NULL,
	segment varchar(70) NOT NULL,
	reason varchar(25) NOT NULL,
	base_year varchar(20) NOT NULL,
	ISO_3166_country_code varchar(10) NOT NULL,
	latitude float NOT NULL,
	longitude float NOT NULL
);