from flask import Flask, jsonify, request

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/home')
def home():
    return "Bienvenido a la página de inicio de mi portafolio"

@app.route('/about-me')
def about_me():
    return "Esta es la página Acerca de Mí"

@app.route('/contact-me')
def contact_me():
    return "Esta es la página de Contacto"

# Retorna la lista `todos` en formato JSON
@app.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos)

# añado una nueva tarea a la lista `todos`
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json  # Convierto el cuerpo de la solicitud en un diccionario
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  # Agrega la nueva tarea a la lista `todos`
    return jsonify(todos)  # Retorna la lista actualizada en formato JSON


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        # Elimimo el todo en la posición indicada
        deleted_todo = todos.pop(position)  # Elimina el todo en la posición dada
        print(f"Deleted todo at position {position}: {deleted_todo}")
        return jsonify(todos), 200  # Retornar la lista actualizada y un código 200 de éxito
    except IndexError:
        # Si la posición no es válida, devuelve un error 404
        return jsonify({"error": "Todo not found"}), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)




