import project


class DataBase:
    def __init__(self):
        self.cur = project.db.connection.cursor()

    def page_users(self, page, per_page, search=''):
        if search:
            args = "%" + search + "%", (page - 1) * per_page, per_page,
            sql = "SELECT SQL_CALC_FOUND_ROWS id, name, email, status " \
                  "FROM user WHERE name LIKE %s LIMIT %s, %s;"
        else:
            args = (page - 1) * per_page, per_page
            sql = "SELECT SQL_CALC_FOUND_ROWS id, name, email, status " \
                  "FROM user LIMIT %s, %s;"
        self.cur.execute(sql, args)
        page_users = self.cur.fetchall()
        self.cur.execute("SELECT FOUND_ROWS();")
        total_users = self.cur.fetchone()
        return page_users, total_users

    def user_get(self, user_id):
        sql = "SELECT name, email, phone, mobile_phone, status " \
              "FROM user WHERE id = %s;"
        self.cur.execute(sql, (user_id,))
        return self.cur.fetchone()

    def user_update(self, id, name, email, phone, mobile_phone, status):
        args = name, email, phone, mobile_phone, status, id
        query = "UPDATE user " \
                "SET name=%s, email=%s, phone=%s, mobile_phone=%s, status=%s " \
                "WHERE id=%s"
        self.cur.execute(query, args)
        project.db.connection.commit()

    def user_create(self, name, email, phone, mobile_phone, status):
        args = name, email, phone, mobile_phone, status
        query = "INSERT INTO user(name, email, phone, mobile_phone, status) " \
                "VALUES(%s,%s,%s,%s,%s)"
        self.cur.execute(query, args)
        result = self.cur.lastrowid
        project.db.connection.commit()
        return result

    def user_courses_get(self, user_id):
        sql = "SELECT course_id " \
              "FROM user_course WHERE user_id = %s;"
        self.cur.execute(sql, (user_id,))
        return self.cur.fetchall()

    def user_delete(self, user_id):
        sql = "DELETE FROM user WHERE id = %s;"
        self.cur.execute(sql, (user_id,))
        delete = self.cur.fetchall()
        if len(delete) == 0:
            project.db.connection.commit()

    def user_courses_update(self, user_id, courses_ids):
        self.cur.execute("DELETE FROM user_course WHERE user_id=%s", (user_id,))
        if courses_ids:
            values = [(user_id, c_id) for c_id in courses_ids]
            self.cur.executemany("INSERT INTO user_course VALUES (%s, %s)", values)
        project.db.connection.commit()

    def courses_get(self):
        sql = "SELECT id, name, code " \
              "FROM course;"
        self.cur.execute(sql)
        return self.cur.fetchall()
