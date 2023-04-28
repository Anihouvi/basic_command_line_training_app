-- Create Databse if not exists

CREATE DATABASE IF NOT EXISTS training;

-- Table: public.progress

-- DROP TABLE IF EXISTS public.progress;

CREATE TABLE IF NOT EXISTS public.progress
(
    id integer NOT NULL DEFAULT nextval('progress_id_seq'::regclass),
    date date,
    time_trained double precision,
    food_eaten character varying(255) COLLATE pg_catalog."default",
    food_type character varying(255) COLLATE pg_catalog."default",
    calories_intake integer,
    calories_burned integer,
    weight_loss double precision,
    CONSTRAINT progress_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.progress
    OWNER to postgres;
