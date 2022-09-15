-- Project Name : チE��コチE
-- Date/Time    : 2022/09/06 21:15:28
-- RDBMS Type   : PostgreSQL
-- Application  : A5:SQL Mk-2

create table high_score_history (
  id INTEGER PRIMARY KEY AUTOINCREMENT
  , chart_id text
  , mode Integer
  , high_score Integer
  , max_combo Integer
  , update_time text
) ;

create table chart_constitution (
  chart_id text
  , music_id text
  , level_id Integer
  , constraint chart_constitution_PKC primary key (chart_id)
) ;

create table rank_history (
  chart_id text not null
  , mode Integer not null
  , rank text
  , count Integer
  , constraint rank_history_PKC primary key (chart_id,mode,rank)
) ;

create table high_score (
  chart_id text not null
  , mode Integer
  , music_id text
  , high_score Integer
  , max_combo Integer
  , play_count Integer
  , cleared_count Integer
  , full_combo_count Integer
  , perfect_count Integer
  , update_time text
  , constraint high_score_PKC primary key (chart_id,mode)
) ;

create table music (
  id text
  , name text
  , artist_id text
  , genre_id text
  , start_date text
  , new_date text
  , end_date text
  , release_month text
  , display_end_date text
  , constraint music_PKC primary key (id)
) ;

create table db_version (
 version text
);
