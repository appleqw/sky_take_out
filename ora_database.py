import cx_Oracle as cx


class ora_database():

    def __init__(self):

        #打开数据库连
        try:
            self.conn=cx.connect('system','orcl','localhost/ORCL')
            print('连接成功')

        except:
            print('连接失败')


    def user_login(self,id,pwd):
        cursor=self.conn.cursor()

        cursor.execute("select 'user_id' from AKA.USER WHERE 'user_id'=%s",id)
        result1=cursor.fetchone()
        if result1=='null':
            return 1 #1表明用户不存在


        cursor.execute("select 'u_code' from AKA.USER WHERE 'user_id'=%s",id)
        result2 = cursor.fetchone()
        if result2!=pwd:
            return 2 #密码错误

        return 3  #转跳登录





        cursor.close()

        return result

