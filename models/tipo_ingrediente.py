from database.db import db

class TipoIngrediente(db.Model):
    __tablename__ = 'Tipos_Ingredientes'

    id = db.Column(db.SmallInteger, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)