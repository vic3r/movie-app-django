-- Table: public.card

-- DROP TABLE public.card;

CREATE TABLE public.card
(
    id integer NOT NULL DEFAULT nextval('card_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "number" integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT card_pkey PRIMARY KEY (id),
    CONSTRAINT "FK_USER_ID" FOREIGN KEY (user_id)
        REFERENCES public.auth_user (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.card
    OWNER to postgres;
