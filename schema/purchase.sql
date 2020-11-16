-- Table: public.purchase

-- DROP TABLE public.purchase;

CREATE TABLE public.purchase
(
    id integer NOT NULL DEFAULT nextval('purchase_id_seq'::regclass),
    user_id integer NOT NULL,
    card_id integer NOT NULL,
    amount money NOT NULL,
    movie_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT purchase_pkey PRIMARY KEY (id),
    CONSTRAINT "FK_CARD_ID" FOREIGN KEY (card_id)
        REFERENCES public.card (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_MOVIE_ID" FOREIGN KEY (movie_id)
        REFERENCES public.movie (imdb_title_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "FK_USER_ID" FOREIGN KEY (user_id)
        REFERENCES public.auth_user (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.purchase
    OWNER to postgres;
