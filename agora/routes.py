from agora import app, database, bcrypt
from agora.models import Usuario
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user
from agora.forms import FormLogin ,FormCriarConta


@app.route("/", methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formLogin.senha.data):
            login_user(usuario)
            return redirect(url_for("bemvindo", usuario=usuario.username))
    return render_template("homepage.html", form=formLogin)

@app.route("/criarconta", methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        bcrypt.check_password_hash
        usuario = Usuario(username=formcriarconta.username.data,
                           email=formcriarconta.email.data, 
                           senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("bemvindo", usuario=usuario.username))
    return render_template("criarconta.html", form=formcriarconta)

@app.route("/bemvindo/<usuario>")
@login_required
def bemvindo(usuario):
    return render_template("bemvindo.html", usuario=usuario)

@app.route('/sair')
@login_required
def sair():
    logout_user()
    return redirect(url_for('homepage'))