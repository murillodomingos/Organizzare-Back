CREATE ROLE "organizzare-org" WITH SUPERUSER;

CREATE USER "organizzare-user" WITH PASSWORD 'organizzare-pass' IN ROLE "organizzare-org";

CREATE DATABASE "organizzare" WITH OWNER "organizzare-back";
