import sqlite3

class dBase:

	def __init__(self, database_file):
		"""Подключаемся к БД и сохраняем курсор соединения"""
		self.connection = sqlite3.connect(database_file)
		self.cursor = self.connection.cursor()

	# def get_count(self, city):
	# 	with self.connection:
	# 		return self.cursor.execute("SELECT COUNT() FROM `city_cords` WHERE `Город` = ?;", (city,)).fetchall()

	# def get_cord\\\\(self, city):
	# 	with self.connection:
	# 		return self.cursor.execute("SELECT `Широта`, `Долгота` FROM `city_cords` WHERE `Город` = ?;", (city,)).fetchall()

	# def get_cord_many(self, city, region):
	# 	with self.connection:
	# 		return self.cursor.execute("SELECT `Широта`, `Долгота` FROM `city_cords` WHERE `Город` = ? AND `Регион` = ?;", (city, region, )).fetchall()

	# def get_region(self, city):
	# 	with self.connection:
	# 		return self.cursor.execute("SELECT `Регион` FROM `city_cords` WHERE `Город` = ?;", (city, )).fetchall()

	# def get_region_2(self, city):
	# 	with self.connection:
	# 		return self.cursor.execute("SELECT `Регион` FROM `city_cords` WHERE `Регион` = ? AND `Город` = '';", (city, )).fetchall()
	def date_first(self):
		with self.connection:
			return self.cursor.execute("SELECT date, week from test ORDER BY week LIMIT 1;").fetchall()

	def date_last(self):
		with self.connection:
			return self.cursor.execute("SELECT date, week from test ORDER BY week DESC LIMIT 1;").fetchall()

	def get_week_for_date(self, date):
		with self.connection:
			return self.cursor.execute("SELECT week from test WHERE date = ? LIMIT 1;", (date)).fetchall()

	def all(self):
		with self.connection:
			return self.cursor.execute("SELECT test.num, test.day, subs.sub, dz.work, dz.hard FROM `test` LEFT JOIN `subs` ON subs.id = test.sub LEFT JOIN `dz` ON dz.id = test.work;").fetchall()

	def add_sub(self, subj):
		with self.connection:
			return self.cursor.execute("INSERT INTO `subs` (sub) VALUES (?);", (subj, )).fetchall()

	def create_lesson(self, week, num, date, day, sub):
		with self.connection:
			return self.cursor.execute("INSERT INTO `test` (week, num, date, day, sub) VALUES (?, ?, ?, ?, ?);", (week, num, date, day, sub)).fetchall()

	def for_one_day(self, week, day):
		with self.connection:
			return self.cursor.execute("SELECT test.num, test.day, subs.sub, test.date, dz.work, dz.hard FROM `test` LEFT JOIN `subs` ON subs.id = test.sub LEFT JOIN `dz` ON dz.id = test.work WHERE test.week = ? AND test.day = ?;", (week, day)).fetchall()

	def for_one_day_pro(self, week, day):
		with self.connection:
			return self.cursor.execute("SELECT test.num, test.day, subs.sub, test.date, dz.work, dz.hard, test.id FROM `test` LEFT JOIN `subs` ON subs.id = test.sub LEFT JOIN `dz` ON dz.id = test.work WHERE test.week = ? AND test.day = ?;", (week, day)).fetchall()

	def add_dz1(self, work):
		with self.connection:
			return self.cursor.execute("INSERT INTO dz (work) VALUES (?);", (work, )).fetchall()

	def add_dz2(self):
		with self.connection:
			return self.cursor.execute("SELECT id FROM dz ORDER BY id DESC LIMIT 1;").fetchall()

	def add_dz3(self, id, dzid):
		with self.connection:
			return self.cursor.execute("UPDATE test SET work = ? WHERE id = ?;", (dzid, id)).fetchall()


	def next_dz1(self, id):
		with self.connection:
			return self.cursor.execute("SELECT sub, work FROM test WHERE id = ?;", (id, )).fetchall()

	def next_dz2(self, sub, id):
		with self.connection:
			return self.cursor.execute("SELECT id FROM test WHERE sub = ? AND id > ? LIMIT 1;", (sub, id)).fetchall()

	def next_dz3(self, dz, ndzid):
		with self.connection:
			return self.cursor.execute("UPDATE test SET work = ? WHERE id = ?;", (dz, ndzid)).fetchall()

	def next_dz4(self, id):
		with self.connection:
			return self.cursor.execute("UPDATE test SET work = NULL WHERE id = ?;", (id, )).fetchall()


	def del_dz(self, id):
		with self.connection:
			return self.cursor.execute("UPDATE test SET work = NULL WHERE id = ?;", (id, )).fetchall()

	def edit_dz(self, dzid, ntext):
		with self.connection:
			return self.cursor.execute("UPDATE dz SET work = ? WHERE id = ?;", (ntext, dzid)).fetchall()

	def check_dz(self, id):
		with self.connection:
			return self.cursor.execute("SELECT work FROM test WHERE id = ?;", (id, )).fetchall()



	def edit_sub1(self, id, sub):
		with self.connection:
			return self.cursor.execute("UPDATE test SET sub = ? WHERE id = ?;", (sub, id)).fetchall()


	def delete_all(self):
		with self.connection:
			return self.cursor.execute("DELETE FROM test;").fetchall()


	def get_dz_by_id(self, id):
		with self.connection:
			return self.cursor.execute("SELECT dz.work FROM `test` JOIN `dz` ON dz.id = test.work AND test.id = ?;", (id, )).fetchall()

