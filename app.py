from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)

    # Configurações do Banco
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o db com o app
    db.init_app(app)

    # Importa e registra o Blueprint
    from routes.tasks_routes import tasks_bp
    app.register_blueprint(tasks_bp)

    # Cria as tabelas automaticamente
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

