import duckdb

con = duckdb("mydatabase.db")

con.execute("CREATE TABLE newtable AS SELECT name FROM mytable")
