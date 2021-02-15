import sqlite3
conn = sqlite3.connect("data.db")
cur = conn.cursor()

sql = """
    CREATE TABLE DataTable (
        Email Varchar,
        Name Varchar,
        StudentID Integer PRIMARY KEY,
        ProjectName Varchar,
        Type Varchar,
        GraduationYear Varchar,
        Abstract Varchar,
        Keyword Varchar,
        Technology Varchar,
        Award Varchar,
        LinkGit Varchar
    ) """

cur.execute(sql)
print("DataTable has been Created")
conn.commit()
conn.close()