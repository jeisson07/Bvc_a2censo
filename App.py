
from flask import Flask,render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL
from numpy import DataSource
app=Flask(__name__)


#Mysql Connection
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='****'
app.config['MYSQL_DB'] ='flask_campaing'

mysql= MySQL(app)

#Guardar datos seetings
app.secret_key='mysecretkey'
@app.route('/')  # 
def Index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT *FROM campaign')
    data=cur.fetchall() #para obtener todos esos datos
    print(data)

    return render_template('index.html',contacts=data)  # cada vez que el usuario visite la ruta inicial

# @app.route('/ASC',methods=['POST'])   #para editar un dato
# def order_ASC():
#     if request.method=='POST':
#         cur=mysql.connection.cursor()
#         cur.execute('SELECT * FROM campaign ORDER BY amount ASC')
#         mysql.connection.commit()
#         data=cur.fetchall()
#     return render_template('index.html',contacts=data) 

# @app.route('/DESC',methods=['POST'])   #para editar un dato
# def order_DESC():
#     if request.method=='POST':
#         cur=mysql.connection.cursor()
#         cur.execute('SELECT * FROM campaign ORDER BY amount DESC')
#         mysql.connection.commit()
#         data=cur.fetchall()
#     return render_template('index.html',contacts=data) 

@app.route('/data', methods=['POST'])
def data():
    if request.method=='POST':
        criterio= request.form.get("sim")
        orden=request.form.get("config")
        print("Este es el criterio: " +criterio)
        print("Orden: "+ orden)
        print(type(orden))
        datos=()
        print(datos)

        if orden=="ASC":
            cur=mysql.connection.cursor()
            cur.execute('SELECT * FROM campaign ORDER BY (%s) ASC',(criterio,))
            mysql.connection.commit()
            datos=cur.fetchall()
            print(datos)
            print("pasa ASC")
        elif orden=='DESC':
            cur=mysql.connection.cursor()
            cur.execute('SELECT * FROM campaign ORDER BY (%s) DESC',(criterio,))
            mysql.connection.commit()
            datos=cur.fetchall()
            print("pasa DESC")
        print(datos)
    return render_template('index.html',contacts=datos) 

if __name__=='__main__':
    app.run(port=300,debug =True)   #iniciar un servidor
