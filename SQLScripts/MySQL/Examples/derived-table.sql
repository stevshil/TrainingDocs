
SELECT SD3.Date, max(`High`) as MaxHigh 
FROM sample_dataset3 AS SD3 
JOIN (select distinct `Date`,abs(`Close`-`Open`) As "range" 
      FROM sample_dataset3 Order by 2 desc limit 3) AS ranges 
ON SD3.Date=ranges.Date Group By 1;

SELECT SD3.Date As `Date`,SD3.Time As "HighTime" 
FROM sample_dataset3 AS SD3 
JOIN (SELECT SD3.Date, max(`High`) as MaxHigh 
FROM sample_dataset3 AS SD3 
JOIN (select distinct `Date`,abs(`Close`-`Open`) As "range" 
      FROM sample_dataset3 Order by 2 desc limit 3) AS ranges 
ON SD3.Date=ranges.Date Group By 1) AS maxHigh
ON SD3.Date=maxHigh.Date and SD3.High=maxHigh.MaxHigh;

SELECT ranges.Date,ranges.range,highTime.HighTime 
FROM (select distinct `Date`,abs(`Close`-`Open`) As "range" 
      FROM sample_dataset3 Order by 2 desc limit 3) AS ranges 
JOIN (SELECT SD3.Date As `Date`,SD3.Time As "HighTime" 
FROM sample_dataset3 AS SD3 
JOIN (SELECT SD3.Date, max(`High`) as MaxHigh 
FROM sample_dataset3 AS SD3 
JOIN (select distinct `Date`,abs(`Close`-`Open`) As "range" 
      FROM sample_dataset3 Order by 2 desc limit 3) AS ranges 
ON SD3.Date=ranges.Date Group By 1) AS maxHigh
ON SD3.Date=maxHigh.Date and SD3.High=maxHigh.MaxHigh) AS highTime
ON ranges.Date=highTime.Date;