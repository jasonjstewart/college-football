import pyodbc 
import requests

YEARS = [
    '2000',
    '2001',
    '2002',
    '2003',
    '2004',
    '2005',
    '2006',
    '2007',  
    '2008',
    '2009',
    '2010',
    '2011',
    '2012',
    '2013',
    '2014',
    '2015',
    '2016',
    '2017',
    '2018',
    '2019'
]

headers = {
    'accept': 'application/json',
}


for year in YEARS:
    print(year)

    #GETS PLAY DATA
    response = requests.get('https://api.collegefootballdata.com/plays?seasonType=regular&year='+year, headers=headers)
    json = response.json()

    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=LAPTOP-G6BR9GBC\SQLEXPRESS;' #server name, this will be whatever your instance is
                        'Database=college-football;' #database name, whatever you name your database
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()

    for item in json:
        id=int(item['id'])
        offense=str(item['offense']) 
        offense_conference=str(item['offense_conference'])
        defense=str(item['defense'])
        defense_conference=str(item['defense_conference'])
        home=str(item['home'])
        away=str(item['away'])
        offense_score=int(item['offense_score'])
        defense_score=int(item['defense_score'])
        drive_id=int(item['drive_id'])
        period=str(item['period'])
        clock=str(item['clock']['minutes']*60+item['clock']['seconds'])
        yard_line=int(item['yard_line'])
        yards_to_goal=int(item['yards_to_goal'])
        down=int(item['down'])
        distance=int(item['distance'])
        yards_gained=int(item['yards_gained'])
        play_type=str(item['play_type'])
        play_text=str(item['play_text'])
        if item['ppa'] is None:
            ppa=0
        else:
            ppa=float(item['ppa'])


        cursor.execute(
            'IF NOT EXISTS(SELECT * FROM dbo.play WHERE id='+str(id)+') '
            +'BEGIN '
            +'INSERT INTO dbo.play ' 
            +'(id,offense,offense_conference,defense,defense_conference,home,away,offense_score,defense_score,drive_id,period,clock,yard_line,yards_to_goal,down,distance,yards_gained,play_type,play_text,ppa)' 
            +'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '
            +'END',
            (id,offense,offense_conference,defense,defense_conference,home,away,offense_score,defense_score,drive_id,period,clock,yard_line,yards_to_goal,down,distance,yards_gained,play_type,play_text,ppa)
        )

    #GETS GAME DATA
    response = requests.get('https://api.collegefootballdata.com/games?seasonType=regular&year='+year, headers=headers)
    json = response.json()

    for item in json:
        id=int(item['id'])
        season=str(item['season'])
        start_date=str(item['start_date'])
        week=int(item['week'])
        season_type=str(item['season_type'])
        neutral_site=str(item['neutral_site'])
        conference_game=str(item['conference_game'])
        if item['attendance'] is None:
            attendance=0
        else:
            attendance=int(item['attendance'])
        home_id=int(item['home_id'])
        home_team=str(item['home_team'])
        home_conference=str(item['home_conference'])
        if item['home_points'] is None:
            home_points=0
        else:
            home_points=int(item['home_points'])
        if item['home_post_win_prob'] is None:
            home_post_win_prob=0
        else:
            home_post_win_prob=float(item['home_post_win_prob'])
        away_id=int(item['away_id'])
        away_team=str(item['away_team'])
        away_conference=str(item['away_conference'])
        if item['away_points'] is None:
            away_points=0
        else:
            away_points=int(item['away_points'])
        if item['away_post_win_prob'] is None:
            away_post_win_prob=0
        else:
            away_post_win_prob=float(item['away_post_win_prob'])
        if item['excitement_index'] is None:
            excitement_index=0
        else:
            excitement_index=float(item['excitement_index'])
        
        cursor.execute(
            'IF NOT EXISTS(SELECT * FROM dbo.game WHERE id='+str(id)+') '
            +'BEGIN '
            +'INSERT INTO dbo.game ' 
            +'(id,season,week,season_type,start_date,neutral_site,conference_game,attendance,home_id,home_team,home_conference,home_points,home_post_win_prob,away_id,away_team,away_conference,away_points,away_post_win_prob,excitement_index )' 
            +'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '
            +'END',
              (id,season,week,season_type,start_date,neutral_site,conference_game,attendance,home_id,home_team,home_conference,home_points,home_post_win_prob,away_id,away_team,away_conference,away_points,away_post_win_prob,excitement_index )
        )

    #Gets drive data
    response = requests.get('https://api.collegefootballdata.com/drives?seasonType=regular&year='+year, headers=headers)
    json = response.json()

    for item in json:
        id=int(item['id'])
        game_id=int(item['game_id'])
        offense=str(item['offense']) 
        offense_conference=str(item['offense_conference'])
        defense=str(item['defense'])
        defense_conference=str(item['defense_conference'])
        scoring=str(item['scoring'])
        start_period=int(item['start_period'])
        start_yardline=int(item['start_yardline'])
        start_yards_to_goal=int(item['start_yards_to_goal'])
        start_time=str(item['start_time'])
        end_period=int(item['end_period'])
        end_yardline=int(item['end_yardline'])
        end_yards_to_goal=int(item['end_yards_to_goal'])
        end_time=str(item['end_time'])
        elapsed=str(item['elapsed'])
        plays=int(item['plays'])
        yards=int(item['yards'])
        drive_result=str(item['drive_result'])

        

        cursor.execute(
            'IF NOT EXISTS(SELECT * FROM dbo.drive WHERE id='+str(id)+') '
            +'BEGIN '
            +'INSERT INTO dbo.drive ' 
            +'(id, game_id, offense, offense_conference, defense, defense_conference, scoring, start_period, start_yardline, start_yards_to_goal, start_time, end_period, end_yardline, end_yards_to_goal, end_time, elapsed, plays, yards, drive_result)' 
            +'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '
            +'END',
            (id, game_id, offense, offense_conference, defense, defense_conference, scoring, start_period, start_yardline, start_yards_to_goal, start_time, end_period, end_yardline, end_yards_to_goal, end_time, elapsed, plays, yards, drive_result)
        )



    conn.commit()


  

