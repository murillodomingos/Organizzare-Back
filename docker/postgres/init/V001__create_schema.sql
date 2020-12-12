\connect "organizzare"

CREATE SCHEMA organizzare_app;

ALTER SCHEMA organizzare_app OWNER TO "organizzare-org";

CREATE TABLE organizzare_app.residents (
    id uuid NOT NULL,
    name text NOT NULL
);

ALTER TABLE organizzare_app.residents OWNER TO "organizzare-org";