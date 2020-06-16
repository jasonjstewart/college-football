with kicker_fg (kicker_name, season, game_id, offense, fg_percentage) AS (
SELECT
	SUBSTRING(p.play_text,1, CHARINDEX(' ', p.play_text, CHARINDEX(' ',p.play_text)+1)) as kicker_name, 
	g.season,
	g.id as game_id,
	p.offense,
	case when 
		sum(case WHEN p.play_type='Field Goal Good' THEN 1 else 0 end)+sum(case WHEN p.play_type='Field Goal Missed' THEN 1 else 0 end)+sum(case WHEN p.play_type='Blocked Field Goal' THEN 1 else 0 end) > 0
	then 	
		ROUND(CAST(sum(case WHEN p.play_type='Field Goal Good' THEN 1 else 0 end) as decimal(10,5))/(CAST(sum(case WHEN p.play_type='Field Goal Good' THEN 1 else 0 end) as decimal(10,5))+CAST(sum(case WHEN p.play_type='Field Goal Missed' THEN 1 else 0 end) as decimal(10,5))+CAST(sum(case WHEN p.play_type='Blocked Field Goal' THEN 1 else 0 end) as decimal(10,5))),5)
	else 0
	end as 'fg_percentage'
	FROM play p
JOIN dbo.drive d on p.drive_id=d.id
JOIN dbo.game g on g.id=d.game_id
WHERE  p.play_type LIKE '%Field Goal%'
GROUP BY SUBSTRING(p.play_text,1, CHARINDEX(' ', p.play_text, CHARINDEX(' ',p.play_text)+1)), g.season, p.offense, g.id
)

select
CAST(p.id as varchar) as id, 
p.offense,
p.offense_conference,
p.defense,
p.defense_conference,
p.home,
p.away,
p.offense_score,
p.defense_score,
p.period,
p.clock,
p.yards_to_goal,
p.down,
p.distance,
SUBSTRING(p.play_text,1, CHARINDEX(' ', p.play_text, CHARINDEX(' ',p.play_text)+1)) as kicker_name,
play_type,
ppa,
d.start_yards_to_goal as drive_start_yard_line,
d.plays as number_of_plays_in_drive,
d.yards as yards_gained_during_drive,
d.drive_result,
g.season,
kfg.fg_percentage,
g.attendance,
p.offense_score-p.defense_score as score_diff

from play p
JOIN drive d on d.id=p.drive_id
JOIN game g on g.id=d.game_id
JOIN kicker_fg kfg on kfg.kicker_name=kicker_name and kfg.season=g.season and kfg.offense=p.offense and g.id=kfg.game_id
WHERE down=4 and play_type NOT IN ('Punt','Penalty','Kickoff','Timeout','Kickoff Return (Offense)','Blocked Punt','Defensive 2pt Conversion','End Period','Blocked Punt Touchdown','Uncategorized','Punt Return Touchdown')
