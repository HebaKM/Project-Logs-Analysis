# Project: Logs Analysis
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an **internal reporting tool** that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions..

## Requirements
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Python3](https://www.python.org/downloads/)
* [psycopg2](http://initd.org/psycopg/docs/install.html)
* Unix-style terminal

## Installation
To run this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

1. Install Vagrant, VirtualBox, and Python3
2. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the [Git software](https://git-scm.com/downloads).
3. Clone or download the [Vagrant VM configuration file](https://github.com/udacity/fullstack-nanodegree-vm)
4. Clone Or download this repository.Then, Paste newsdb.py from this project into the vagrant/ sub-directory
5. Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

## Steps to run this project
1. Open terminal and navigate to the FSND-Virtual-Machine directory, then run the command: `cd vagrant`.
2. Inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it.
3. Next, log into the virtual machine.: `vagrant up vagrant ssh`
4. Inside the VM, change directory to /vagrant: `cd /vagrant`
5. run the command `psql -d news -f newsdata.sql` to connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data
6. Run the command `psql news` to connect to the news database. Then run the following queries to create the views needed to run the queries:  

```sql
CREATE VIEW error_total AS
    (SELECT DATE(time) AS date, COUNT(*) AS num
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP BY date
    ORDER BY date);
```
```sql
CREATE VIEW total AS
    (SELECT DATE(time) AS date, COUNT(*) AS num
    FROM log
    GROUP BY date
    ORDER BY date);
```
7. Lastly, run `python logs-analysis.py`.    
