import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='cedb002',
                             db='python_RPi',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:

    with connection.cursor() as cursor:
        sql = "INSERT INTO `lecteurs` (`nom`, `email`, `mot_de_passe`) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('lemaitre', 'python_rpi@python.org', 'mdp'))

    connection.commit()

    with connection.cursor() as cursor:
        sql = "SELECT `id`, `nom`, 'mot_de_passe' FROM `lecteurs` WHERE `email`=%s"
        cursor.execute(sql, ('python_rpi@python.org',))
        result = cursor.fetchone()
        print(result)
        print(result['nom'])
finally:
    connection.close()
