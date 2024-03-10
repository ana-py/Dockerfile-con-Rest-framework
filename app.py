from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

def student_exists(student_id):
    return next((student for student in students if student['id'] == student_id), None)

@app.route('/alumnos', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/alumnos', methods=['POST'])
def create_student():
    new_student = request.json
    if not new_student.get('id'):
        new_student['id'] = (len(students) + 1)
    if student_exists(new_student['id']):
        return jsonify({'message': 'Student ID already exists'}), 400
    students.append(new_student)
    return jsonify({'message': 'Student created'}), 201

@app.route('/alumnos/<int:student_id>', methods=['PUT'])
def edit_alumn(student_id):
    student = student_exists(student_id)
    if student:
        if request.json.get('id') and request.json['id'] != student_id:
            return jsonify({'message': 'Student ID cannot be modified'}), 400
        student.update(request.json)
        return jsonify({'message': 'Student updated'}), 200
    return jsonify({'message': 'Student not found'}), 404

@app.route('/alumnos/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = student_exists(student_id)
    if student:
        students.remove(student)
        return jsonify({'message': 'Student deleted'}), 200
    return jsonify({'message': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')