\connect "organizzare"

CREATE SCHEMA organizzare_app;

ALTER SCHEMA organizzare_app OWNER TO "organizzare-org";

CREATE TABLE organizzare_app.condominium (
    id uuid NOT NULL,
    name text NOT null,
    cep varchar(8) not null,
    address text not null,
    number text not null,
    city text not null,
    primary key (id)
);

ALTER TABLE organizzare_app.condominium OWNER TO "organizzare-org";

CREATE TABLE organizzare_app.apartments (
    id uuid NOT NULL,
    number text NOT null,
    block text NOT null,
    condominium uuid not null,
    foreign key (condominium) references organizzare_app.condominium(id),
    primary key (id)
);

ALTER TABLE organizzare_app.apartments OWNER TO "organizzare-org";

CREATE TABLE organizzare_app.residents (
    id uuid NOT NULL,
    name text NOT null,
    cpf varchar(11) not null,
    register_timestamp timestamp with time zone not null,
    unregister_timestamp timestamp with time zone null, 
    apartment_id uuid not null,
    foreign key (apartment_id) references organizzare_app.apartments(id), 
    primary key (id)
);

ALTER TABLE organizzare_app.residents OWNER TO "organizzare-org";

create table organizzare_app.bills(
	id uuid not null,
	bill_type text not null,
	register_timestamp timestamp with time zone not null,
    due_timestamp timestamp with time zone not null,
    value decimal (10,2) not null,
    code text not null,
    resident uuid not null,
    foreign key (resident) references organizzare_app.residents(id),
    primary key (id)
);

ALTER TABLE organizzare_app.bills OWNER TO "organizzare-org";

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";