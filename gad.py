
import os
from flask import Flask, jsonify, request
import hashlib

app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    return 'Inicio'

@app.route('/status', methods=['GET'])
def estado():
    return app.make_response(("status 201",201))

@app.route('/validarFirma', methods=['POST'])
def validacion():    

    hash_entregado = request.form['hash']
    mensaje_entregado = request.form['mensaje']
    mensaje_a_byte = mensaje_entregado.encode('utf-8')
    mensaje_hasheado = hashlib.sha256(mensaje_a_byte)
    string_hahseado = mensaje_hasheado.hexdigest()
    string_en_lower = string_hahseado.upper()

    if string_en_lower == hash_entregado:
        respuesta = {'valido': True, 'mensaje': mensaje_entregado} 
    else:
        respuesta = {'valido': False, 'mensaje': mensaje_entregado} 

    respuesta_final =  jsonify(respuesta)

    return respuesta_final


if __name__ == '__main__':
    port = int(os.environ.get('Port',5000))
    app.run(host='0.0.0.0', port = port)





