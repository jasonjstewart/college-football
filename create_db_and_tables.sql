USE master
IF EXISTS(select * from sys.databases where name='college_football')
DROP DATABASE college_football

CREATE DATABASE college_football

IF OBJECT_ID('dbo.play', 'U') IS NOT NULL 
drop table play;

create table play(
	 id bigint primary key
	,offense varchar(50)
	,offense_conference varchar(20)
	,defense varchar(50)
	,defense_conference varchar(20)
	,home char(50)
	,away varchar(50)
	,offense_score bigint
	,defense_score bigint
	,drive_id bigint
	,period int
	,clock varchar(150)
	,yard_line int
	,yards_to_goal int
	,down int
	,distance int
	,yards_gained int
	,play_type varchar(200)
	,play_text varchar(1000)
	,ppa decimal(18,16)
);

IF OBJECT_ID('dbo.game', 'U') IS NOT NULL 
drop table game;

create table game(
	id bigint
	,season int
	,week int
	,season_type varchar(15)
	,start_date varchar(50)
	,neutral_site varchar(50)
	,conference_game varchar(30)
	,attendance int
	,home_id bigint
	,home_team varchar(50)
	,home_conference varchar(20)
	,home_points int
	,home_post_win_prob decimal(18,4)
	,away_id bigint 
	,away_team varchar(50)
	,away_conference varchar(20)
	,away_points int
	,away_post_win_prob decimal(18,4)
	,excitement_index decimal(18,6)
)

IF OBJECT_ID('dbo.drive', 'U') IS NOT NULL 
drop table drive;

create table drive(
	 id bigint primary key
	,game_id bigint
	,offense varchar(50)
	,offense_conference varchar(20)
	,defense varchar(50)
	,defense_conference varchar(20)
	,scoring varchar(6)
	,start_period bigint
	,start_yardline bigint
	,start_yards_to_goal bigint
	,start_time varchar(150)
	,yard_line int
	,yards_to_goal int
	,end_period int
	,end_yardline int
	,end_yards_to_goal int
	,end_time varchar(150)
	,elapsed varchar(150)
	,plays int
	,yards int
	,drive_result varchar(50)
);
