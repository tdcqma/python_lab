# 查询当前数据库
SELECT DATABASE();

# 查看当前数据库有哪些表
SHOW TABLES;

# 删除多余的表
DROP TABLE department;
DROP TABLE employee;
DROP TABLE table1;
DROP TABLE table2;

# 从init.sql文件中导入，需要在终端操作
# source /Users/mahaibin/init.sql

# 1、查询所有的课程的名称以及对应的任课老师姓名
SELECT course.cname,teacher.tname 
FROM course
INNER JOIN teacher ON course.teacher_id = teacher.tid;
	#生物	张磊老师
	#物理	李平老师
	#美术	李平老师
	#体育	刘海燕老师

# 2、查询学生表中男女生各有多少人
SELECT gender 性别, COUNT(gender) FROM student GROUP BY gender;
	#女	6
	#男	10

# 3、查询物理成绩等于100的学生的姓名
SELECT
	student.sname
FROM
	student
WHERE
	sid IN (
		SELECT 
			student_id
		FROM 
			score 
		INNER JOIN course ON score.course_id = course.cid
		WHERE num = 100
		AND course_id = 2
		);
	#张四
	#铁锤
	#李三

# 4、查询平均成绩大于八十分的同学的姓名和平均成绩
# 表格：score、student
SELECT
	student.sname,
	t1.avg_num
FROM
	student
INNER JOIN (	
	SELECT
		student_id,
		avg(num) AS avg_num
	FROM
		score
	GROUP BY
		student_id
	HAVING
		avg(num) > 80
	) as t1 on student.sid = t1.student_id;
	#张三	82.2500
	#刘三	87.0000

#5、查询所有学生的学号，姓名，选课数，总成绩(注意：对于那些没有选修任何课程的学生也算在内)
SELECT
	student.sid,
	student.sname,
	t1.course_num,
	t1.total_num
FROM
	student
LEFT JOIN (
	SELECT
		student_id,
		COUNT(course_id) course_num,
		SUM(num) total_num
	FROM
		score
	GROUP BY
		student_id
) AS t1 ON student.sid = t1.student_id;
	#1	理解	3	85
	#2	钢蛋	3	175
	#3	张三	4	329
	#4	张一	4	257
	#5	张二	4	257
	#6	张四	4	276
	#7	铁锤	4	264
	#8	李三	4	264
	#9	李一	4	268
	#10	李二	4	297
	#11	李四	4	297
	#12	如花	4	297
	#13	刘三	1	87
	#14	刘一		
	#15	刘二		
	#16	刘四		
	
#6、 查询姓李老师的个数
SELECT
	COUNT(tname) 个数
FROM
	teacher
WHERE
	tname LIKE '李%';
	#2

#7、 查询没有报李平老师课的学生姓名(找出报名李平老师课程的学生，然后取反就可以)
# teacher表、student表,course表
# 分析过程
# 7.1 首先需要找出李平老师都讲哪些课，找出对应的课程id，即cid。
SELECT course.cid FROM course
INNER JOIN teacher ON course.teacher_id = teacher.tid
WHERE teacher.tname='李平老师';

# 7.2 知道了李平老师讲的课程ID（cid）后，找出选择这些课程ID的学生，
# 注意，学生可能选择其中一门课程，也可能选择多门课程，如果选择多门课程则筛选出的student_id就会出现多次，
# 因此需要借助distinct来去重。
SELECT DISTINCT score.student_id FROM score
WHERE course_id IN (2,4);

# 7.3 上一步已经拿到了学习李平老师学生的id，即score.student_id,
# 接下来在学生里表里搜索除去这些ID以外的学生名即可，将7.1与7.2添加到7.3中后如下所示：

SELECT student.sname FROM student
WHERE sid NOT IN (
	SELECT DISTINCT score.student_id FROM score
	WHERE course_id IN (
		SELECT course.cid FROM course
		INNER JOIN teacher ON course.teacher_id = teacher.tid
		WHERE teacher.tname='李平老师'
	)
);
	#刘三
	#刘一
	#刘二
	#刘四

