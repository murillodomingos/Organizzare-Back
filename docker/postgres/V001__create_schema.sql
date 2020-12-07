\connect "organizzare"

CREATE SCHEMA organizzare-app;

ALTER SCHEMA organizzare-app OWNER TO "organizzare-org";

CREATE TABLE organizzare-app.residents (
    id uuid NOT NULL,
    name string NOT NULL
);

ALTER TABLE organizzare-app.residents OWNER TO "organizzare-org";