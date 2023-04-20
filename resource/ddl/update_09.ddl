CREATE TABLE degrees (
  id text
  , name text
  , category text
  , mission_label text
  , created_at text
  , updated_at text
  , CONSTRAINT degrees_PKC PRIMARY KEY (id)
) ;

CREATE TABLE character (
  id text
  , name text
  , introduction text
  , dearness_rank Integer
  , dearness_point Integer
  , is_used boolean
  , sort_index Integer
  , costume_id text
  , collaboration boolean
  , dearness_ranking Integer
  , ranking_get_date text
  , updated_at text
  , CONSTRAINT character_PKC PRIMARY KEY (id)
) ;