import unittest
from app import app, db, init_db
from models.producto import Producto
from models.producto_ingrediente import ProductoIngrediente
from models.heladeria_producto import HeladeriaProducto
from models.heladeria import Heladeria

class TestHeladeria(unittest.TestCase):

    pass
    # def setUp(self):
    #     init_db(app)
    #     with app.app_context():
    #         producto_copa = Producto(id=21, nombre="Copa de Prueba", precio=30000.0\
    #                                     , tipo_vaso="", volumen= 300, id_tipo_producto = 1 )

    #         #relacioamos 2 ingredientes al producto
    #         producto_copa_ingredediente_1 = ProductoIngrediente(id_producto=21, id_ingrediente=1)
    #         producto_copa_ingredediente_2 = ProductoIngrediente(id_producto=21, id_ingrediente=2)

    #         producto_copa_habilitar = HeladeriaProducto(id_heladeria= 1, id_producto=21)

    #         db.session.add(producto_copa)
    #         db.session.add(producto_copa_ingredediente_1)
    #         db.session.add(producto_copa_ingredediente_2)
    #         db.session.add(producto_copa_habilitar)

    #         db.session.commit()    

    # def tearDown(self):
    #     with app.app_context():
    #         Producto.eliminar_por_id(21)           

    # def test_calcular_producto_mas_rentable(self):
    #     with app.app_context():
    #         producto_mas_rentable = Heladeria.calcular_producto_mas_rentable()
    #         self.assertEqual(producto_mas_rentable.nombre, "Copa de Prueba")            

    #def test_vender_producto(self):
