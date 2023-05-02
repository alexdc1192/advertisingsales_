from flask import Flask, jsonify, request
import os
import pickle

# EJERCICIO APIS

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/', methods=['GET'])
def home():
    return """
    <h1>APP para calcular la predicción de ventas 
    a partir de todos los valores de gastos en publicidad</h1>
    APP para testear flask y Railway
    """

# Ruta para la predicción
@app.route('/predict', methods=['GET'])
def predict():
    tv = request.args['tv']
    radio = request.args['radio']
    newspaper = request.args['newspaper']

    loaded_model = pickle.load(open('model.pkl', 'rb'))

# Carga de nuevos datos con los que predecir las ventas
    new_data = [tv, 
                radio, 
                newspaper]

    prediction = loaded_model.predict([new_data])
    return jsonify({'Con los datos introducidos, las ventas serían de': prediction[0]})


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(port=5000)