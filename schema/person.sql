-- Table: public.person

-- DROP TABLE public.person;

CREATE TABLE public.person
(
    imdb_name_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    birth_name character varying(400) COLLATE pg_catalog."default" NOT NULL,
    height integer,
    bio text COLLATE pg_catalog."default",
    birth_details character varying(200) COLLATE pg_catalog."default",
    date_of_birth character varying COLLATE pg_catalog."default",
    place_of_birth character varying(200) COLLATE pg_catalog."default",
    death_details text COLLATE pg_catalog."default",
    date_of_death character varying(100) COLLATE pg_catalog."default",
    place_of_death character varying(200) COLLATE pg_catalog."default",
    reason_of_death character varying(200) COLLATE pg_catalog."default",
    spouses_string text COLLATE pg_catalog."default",
    spouses integer,
    divorces integer,
    spouses_with_children integer,
    children integer,
    id integer NOT NULL DEFAULT nextval('films_person_id_seq'::regclass),
    CONSTRAINT person_pkey PRIMARY KEY (imdb_name_id)
)

TABLESPACE pg_default;

ALTER TABLE public.person
    OWNER to postgres;
