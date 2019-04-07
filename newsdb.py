#!/usr/bin/env python3
import psycopg2

DBNAME = "news"

query_1 = """SELECT title, count(*) AS views
             FROM articles, log
             WHERE path LIKE CONCAT('/article/', slug)
             GROUP BY title
             ORDER BY views DESC
             LIMIT 3;"""

query_2 = """SELECT name, count(*) AS views
             FROM log
             JOIN articles
             ON CONCAT('/article/', articles.slug) = log.path
             JOIN authors
             ON (authors.id = articles.author)
             GROUP BY name
             ORDER BY views DESC;"""

query_3 = """SELECT error_total.date,
             ROUND((CAST(error_total.num AS NUMERIC) / total.num) * 100, 2)
             AS error_rate
             FROM error_total
             JOIN total
             ON error_total.date = total.date
             WHERE (CAST(error_total.num AS NUMERIC) / total.num) * 100 > 1;"""


def print_results(results, question):
    """Prints the results obtained from the database."""
    row_format = "\n* {} - {} views"
    print(question)
    for row in results:
        print(row_format.format(row[0], str(row[1])))


def get_day():
    """Return the day on which more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_3)
    day = c.fetchall()
    db.close()

    question = "\n3.On which days did more than 1% of requests lead to errors?"
    row_format = "\n* {} - {}% errors"
    print(question)
    print(row_format.format(day[0][0], str(day[0][1])))


def run_query(question, query):
    """Return all authors/articles from the database, ordered by their
    popularity/views."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()

    print_results(results, question)


if __name__ == '__main__':
    run_query("1.What are the most popular three articles of all time?",
              query_1)
    run_query("\n2.Who are the most popular article authors of all time?",
              query_2)
    get_day()
