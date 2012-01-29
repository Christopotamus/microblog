BEGIN;
CREATE TABLE "wuphf_author" (
    "id" serial NOT NULL PRIMARY KEY,
    "username" varchar(40) NOT NULL,
    "password" varchar(40) NOT NULL
)
;
CREATE TABLE "wuphf_wuphf" (
    "id" serial NOT NULL PRIMARY KEY,
    "author_id" integer NOT NULL REFERENCES "wuphf_author" ("id") DEFERRABLE INITIALLY DEFERRED,
    "text" varchar(140) NOT NULL
)
;
CREATE INDEX "wuphf_wuphf_author_id" ON "wuphf_wuphf" ("author_id");
COMMIT;
