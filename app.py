from flask import Flask , request, jsonify
from models.task import Task


 #__name__ = "__main__"
app = Flask(__name__)

#CRUD
#Create,Read,Uptade and Delete = Criar,Let,Atualizar e Deletar

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_taks():
    global task_id_control
    data = request.get_json()
    new_task = Task(title=data["title"],description=data.get("decription",""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"mensagem": "Nova tarefa criada com sucesso"})


@app.route("/tasks",methods=["GET"])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())

    output = {
            "tasks": task_list,
            "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:id>",methods=["GET"])
def get_task(id):
    task = None
    for t in tasks :
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"menssage": "Não foi possível encontrar a atividade"}),404

@app.route("/tasks/<int:id>",methods=["PUT"])
def update_task(id):

    task = None
    for t in tasks:
        if t.id == id :
            task = t
    print(task)
    if task == None:
        return jsonify({"menssage": "Tarefa atualizada com sucesso"}),404

    data =request.get_json()
    task.title = data["title"]
    task.description = data["descrpition"]
    task.completed = data["completed"]
    print(task)
    return jsonify({"menssage": "Tarefa atualizada com sucesso"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    task = None

    for t in tasks:
        if t.id == id:
            task = t
            break

    if task is None:
        return jsonify({
            "mensagem": "Tarefa não encontrada"
        }), 404

    tasks.remove(task)

    return jsonify({
        "mensagem": "Tarefa deletada com sucesso"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)

