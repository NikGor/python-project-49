from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(name='Games Admin', template_mode='bootstrap3')


class GameAdminView(ModelView):
    column_labels = {'name': 'Name', 'description': 'Description'}
