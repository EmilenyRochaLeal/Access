from agora import database, app
from agora.models import Usuario
# db browser
with app.app_context():
    database.create_all()