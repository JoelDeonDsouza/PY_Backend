from flask import request, jsonify
from config import app, db
from models import User


# GET USERS //
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    json_user = list(map(lambda x: x.to_json(), users))
    return jsonify({"users": json_user})


# CREATE USERS //
@app.route("/create_user", methods=["POST"])
def create_user():
    name = request.json.get("name")
    email = request.json.get("email")
    # condition //
    if not name or not email:
        return (jsonify({"message": "Name and Email fields are required"}), 400)
    # check condition //
    new_user = User(name=name, email=email)
    try:
        db.session.add(new_user)
        db.session.commit()
    # if error condition //
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    # user created //
    return jsonify({"message": "User created"}), 201


# UPDATE USERS //
@app.route("/update_user/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    user = User.query.get(user_id)
    # condition //
    if not user:
        return jsonify({"message": "User not found"}), 404
    # patch //
    user_data = request.json
    user.name = user_data.get("name", user.name)
    user.email = user_data.get("email", user.email)
    # save session //
    db.session.commit()
    return jsonify({"message": "User update"}), 201


# DELETE USERS //
@app.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    # condition //
    if not user:
        return jsonify({"message": "User not found"}), 404
    # delete user //
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200


# Run app //
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
