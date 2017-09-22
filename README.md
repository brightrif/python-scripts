# python-scriptss
1) storage log files into mysql datbase 
    +-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| ip        | varchar(15)  | YES  |     | NULL    |       |
| date      | date         | YES  |     | NULL    |       |
| time      | time         | YES  |     | NULL    |       |
| method    | varchar(30)  | YES  |     | NULL    |       |
| url       | varchar(500) | YES  |     | NULL    |       |
| referance | varchar(500) | YES  |     | NULL    |       |
| status    | varchar(100) | YES  |     | NULL    |       |
| bytes     | varchar(10)  | NO   |     | NULL    |       |
| timetaken | varchar(10)  | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+

