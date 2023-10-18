-- Heaviest Hitters

with t as
	(select 
		batting.yearid as yearid , 
		batting.team_id as team_id,
		round(avg(people.weight), 2) as avg_weight
	from batting
	inner join people  
		on batting.playerid = people.playerid 
	group by 1, 2)
select t.yearid, teams.name, t.avg_weight from t
inner join teams
	on t.team_id = teams.id 
where (t.yearid, t.avg_weight) 
	in
		(select t.yearid, max(t.avg_weight) 
		from t 
		group by t.yearid)
order by 1 desc 
;


-- Shortest Sluggers
select 
	batting.yearid , 
	teams.name,  
	round(avg(people.height), 2) as "Avg Height"
from batting
inner join people  
	on batting.playerid = people.playerid 
inner join teams
	on batting.team_id  = teams.id 
where batting.yearid = 2019
group by 1, 2
order by 3;


-- Biggest Spenders

with t as
(SELECT 
  salaries.yearid AS y,
  teams.name AS teamname,
  SUM(salary) as total
FROM salaries
INNER JOIN teams
	ON teams.teamid = salaries.teamid
GROUP BY 1,2)
select * from t
where
(y, total)
in
(select y, max(total) from t group by y)
order by 1 desc;


-- Most Bang For Their Buck In 2010

select teams.name as "Team Name", round((sum(salaries.salary)/teams.w)::numeric , 2) as "Cost per Win"
from salaries 
join teams 
on salaries.team_id = teams.id
where salaries.yearid = 2010
group by teams.w, 1
order by 2 desc;
