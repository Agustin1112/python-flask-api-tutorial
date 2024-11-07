from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# Listado de tareas
todos = [
    { "label": "Comprar leche", "done": False },
    { "label": "Llamar al dentista", "done": False },
    { "label": "Enviar reporte", "done": True },
    { "label": "Hacer ejercicio", "done": False },
    { "label": "Leer un libro", "done": True },
]

# Ruta para la raíz (home)
@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Todo API!</h1>"

# Ruta para obtener todas las tareas
@app.route('/todos', methods=['GET'])
def get_todos():
    response = jsonify(todos)  # Devuelvo la lista de todos en formato JSON
    response.headers['Content-Type'] = 'application/json'  # Aseguro que la respuesta sea en JSON
    return response, 200

# Ruta para agregar una nueva tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()

    
    if not request_body or 'label' not in request_body:
        return jsonify({"error": "Missing 'label' in request body"}), 400
    
    new_todo = {
        "label": request_body['label'],
        "done": False
    }
    
    todos.append(new_todo)
    return jsonify(new_todo), 201 #(Devuelvo la tarea creada)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 1 or position > len(todos):
        return jsonify({"error": "Invalid task position"}), 404

    position_updated = position - 1
    deleted_todo = todos.pop(position_updated)  
    return jsonify(deleted_todo), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)




