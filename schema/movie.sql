
CREATE TABLE public.movie
(
    imdb_title_id character varying(30) COLLATE pg_catalog."default" NOT NULL,
    title character varying(200) COLLATE pg_catalog."default" NOT NULL,
    original_title character varying(200) COLLATE pg_catalog."default" NOT NULL,
    year character varying(100) COLLATE pg_catalog."default",
    date_published character varying(20) COLLATE pg_catalog."default",
    genre character varying(50) COLLATE pg_catalog."default",
    duration integer,
    country character varying(500) COLLATE pg_catalog."default",
    language character varying(500) COLLATE pg_catalog."default",
    director character varying(100) COLLATE pg_catalog."default",
    writer character varying(100) COLLATE pg_catalog."default",
    production_company character varying(200) COLLATE pg_catalog."default",
    actors text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    avg_vote double precision,
    votes integer,
    budget character varying(100) COLLATE pg_catalog."default",
    usa_gross_income character varying(100) COLLATE pg_catalog."default",
    worldwide_gross_income character varying(100) COLLATE pg_catalog."default",
    metascore double precision,
    reviews_from_users double precision,
    reviews_from_critics double precision,
    id integer NOT NULL DEFAULT nextval('films_film_id_seq'::regclass),
    CONSTRAINT movie_pkey PRIMARY KEY (imdb_title_id)
)

TABLESPACE pg_default;

ALTER TABLE public.movie
    OWNER to postgres;
