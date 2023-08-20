"""

1. Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code, use this link: https://datahub.io/core/continent-codes
"""
import sqlite3
#
connection = sqlite3.connect("geography.db")
#
cursor = connection.cursor()
#
# cursor.execute(
#     """
#     CREATE TABLE Continents (
#     continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     continent_name TEXT NOT NULL,
#     continent_code CHAR(2) NOT NULL
#     );
#     """
# )
"""
2. Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
"""

# continents_list = [
#     ('Asia', 'AS'),
#     ('Africa', 'AF'),
#     ('North America', 'NA'),
#     ('South America', 'SA'),
#     ('Oceania', 'OC'),
#     ('Europe', 'EU'),
#     ('Antartica', 'AN')
# ]
#
# sql_query = "INSERT INTO Continents (continent_name, continent_code) VALUES (?, ?)"
#
# cursor.executemany(sql_query, continents_list)
# connection.commit()

"""
3. Write a SQL statement to create a table called countries, with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_id – foreign key
population – number
"""
cursor.execute(
    """
    CREATE TABLE Continents (
    continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT NOT NULL,
    continent_code CHAR(2) NOT NULL
    );
    """
)
"""
4. Write a few SQL statements to add some countries. Here is a list of countries with their codes.
Feel free to invent or approximate their populations,
 and use your geography knowledge for their continent.
Add at least 10 countries, as diverse as possible (INSERT). Examples:
– Romania, EU, 19mil
– USA, NA, 330mil
– France, EU, 70mil
– Hungary, EU,  9mil
– Canada, NA, 40mil
– China, AS, 1450mil
– Belgium, EU, 12mil
–  Egypt, AF, 110mil
– Australia, OC, 25mil
"""

"""
5. Write a SQL statement to select all countries, ordered by name. Write another statement to count them all.
"""

"""
6. Write a SQL statement to select only countries with a population greater than 20 millions.
"""

"""
7. Write a SQL statement to select only countries that start with a certain letter (choose one that exists for you, e.g. C in the example above).
"""

"""
8. Write a SQL statement that groups all countries by continents, and counts them.
"""

"""
9. Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).
"""

"""
10.Extra exercises can be found online:
W3Schools: https://www.w3schools.com/mysql/exercise.asp?filename=exercise_select1
OneCompiler: https://onecompiler.com/mysql

"""