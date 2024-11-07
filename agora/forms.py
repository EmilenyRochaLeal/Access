from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from agora.models import Usuario

class FormLogin(FlaskForm):  # Corrigido para herdar de FlaskForm
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao = SubmitField("Entrar")

class FormCriarConta(FlaskForm):  # Corrigido para herdar de FlaskForm
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 12)])
    validator_senha = PasswordField("Confirme sua senha", validators=[DataRequired(), EqualTo('senha')])
    yes_senha = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado, faça login para continuar")  # Levanta o erro em vez de retornar
