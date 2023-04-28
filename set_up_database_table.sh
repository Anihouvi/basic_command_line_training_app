#!/bin/bash

# Specify your database credentials
DB_USER="your_database_user"
DB_PASS="your_database_password"
DB_HOST="your_database_host"
DB_PORT="your_database_port"

# SQL commands to create the database and table
SQL_COMMANDS=$(cat <<-END
    CREATE DATABASE IF NOT EXISTS training;

    \c training;

    CREATE TABLE IF NOT EXISTS public.progress
    (
        id serial PRIMARY KEY,
        date date,
        time_trained double precision,
        food_eaten character varying(255),
        food_type character varying(255),
        calories_intake integer,
        calories_burned integer,
        weight_loss double precision
    );

    ALTER TABLE public.progress
        OWNER to postgres;
END
)

# Execute the SQL commands using psql
echo "$SQL_COMMANDS" | psql -U $DB_USER -h $DB_HOST -p $DB_PORT -W $DB_PASS

