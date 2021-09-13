#https://www.youtube.com/watch?v=IgCfZkR8wME&ab_channel=FaztCode
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask (__name__)
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)



app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        company = request.form['company']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (fullname, phone, company) VALUES (%s,%s,%s)", 
        (fullname, phone, company))
        mysql.connection.commit()
        flash('Contacto Agregado Satisfactoriamente')
        return redirect(url_for('Index'))


@app.route('/edit/<id>', methods = ['GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM contacts WHERE id = {id}")
    #cur.execute(f'SELECT * FROM contacts WHERE id = (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        company = request.form['company']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts 
            SET fullname = %s, 
            company = %s, 
            phone = %s
        WHERE id = %s
        """,(fullname, company, phone,id))
        mysql.connection.commit()
        flash('Contacto Actualizado Satisfactoriamente')
        return(redirect(url_for('Index')))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado Satisfactoriamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
