import getpass
import oracledb

#pw = getpass.getpass("Enter password: ")

connection = oracledb.connect(
    user="willianUser",
    password="senha",
    dsn="localhost/xe")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# Create a table

'''cursor.execute("""
    begin
        execute immediate 'drop table todoitem';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")'''

cursor.execute("""
    create table amostras (
        id number generated always as identity,
        so number(4,2),
        creation_ts timestamp with time zone default current_timestamp,
        done number(1,0),
        primary key (id))""")

# Insert some data

rows = [ ("Task 1", 1 ),
         ("Task 2", 0 ),
         ("Task 3", 1 ),
         ("Task 4", 0 ),
         ("Task 5", 1 ) ]

cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# Now query the rows back
for row in cursor.execute('select description, done from todoitem'):
    if (row[1]):
        print(row[0], "is done")
    else:
        print(row[0], "is NOT done")