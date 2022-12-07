from typing import List, Any
from urllib.request import Request, urlopen
import re
import mysql.connector as mysql

dd: str = ''
url: str = ''
a: str = ''
theme: str = ''
scripts: List[Any] = []
c = []
MY_HOST = 'localhost'
MY_USER = 'Testing'
MY_PASS = 'Gde&3$E8rmh6'

try:
    mysql_db = mysql.connect(host=MY_HOST, user=MY_USER, password=MY_PASS, database='websites')
    mysql_cur = mysql_db.cursor(buffered=True)
    mysql_cur.execute("SHOW VARIABLES WHERE variable_name = 'version'")
    print(f"MySQL server version: {mysql_cur.fetchone()[1]}")
except mysql.Error as err:
    print(f"mysql error: {err}")
    exit(1)

with open('website_list.txt') as file:
    lines = [line.rstrip() for line in file]

#print(lines)

for line in lines:
    wp = Request(
        url=line,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'})
    pw = urlopen(wp).read()

    if re.search('/wp-content/themes/', str(pw)):
        a = re.findall(r"/wp-content\/themes\b/[a-zA-Z-_]+/", str(pw))
        # print(a)
        theme = a[0]
        theme = theme.replace('/wp-content/themes/', '')
        theme = theme.replace('/', '')
        a.clear()
        if re.search('(?<=<script)(.*?)(?=script>)', str(pw)):
            #print('Printing  Scripts list')
            scripts = re.findall(r"(?<=<script)(.*?)(?=script>)", str(pw))

        print('\n')
        print('=============================================')
        print(line)
        if re.search('/wp-content/plugins/', str(pw)):
            plugins = re.findall(r"/wp-content\/plugins\b/[a-zA-Z_-]+/", str(pw))
        for ii in plugins:
            if ii not in c:
                c.append(ii)
        if re.search('gtag', str(pw)):
            print('It runs Google Analytics')
            dd='Yes'
        else:
            print('No Google Analytics')
            dd='No'
        mysql_cur.execute("insert into w_list (name,analytics,theme) values ('"+ line +"','"+ str(dd)+"','"+theme+"');")
        mysql_db.commit()
        mysql_cur.execute("select * from w_list where name = '"+line+"';")
        ee=mysql_cur.fetchone()[0]
        for jj in range(0, len(c)):
            c[jj] = c[jj].replace('/wp-content/plugins/', '')
            c[jj] = c[jj].replace('/', '')
            mysql_cur.execute("insert into plugins (w_id,w_plugin) values ('"+ str(ee) +"','" + str(c[jj]) + "');")
            mysql_db.commit()
        print('Wordpress Theme: ' + theme)
        print(c)
        c.clear()
        for i in range(0, len(scripts)):
            mysql_cur.execute("insert into scripts (w_id,w_script) values ('" + str(ee) + "','" + str(scripts[i]) + "');")
            mysql_db.commit()
        # print(scripts[i])
        # print('\n')
        scripts.clear()
    else:
        print('\n')
        print('=============================================')
        print(line)
        print('No Wordpress')
        mysql_cur.execute("insert into nowp (nw_list) values ('"+ line +"');")
        mysql_db.commit()