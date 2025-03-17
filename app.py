from flask import Flask, jsonify

todo = Flask('__name__')

students = [
    {
        'id': 1,
        'student_name': 'kee',
        'age': 21,
        'email': 'hello@gmail.com'
    },
    {
        'id': 2,
        'student_name': 'pa',
        'age': 21,
        'email': 'pavan@gmail.com'
    },
    {
        'id': 3,
        'student_name': 'nik',
        'age': 21,
        'email': 'hi@gmail.com'
    }
]

@todo.route('/students-list')
def students_list():
    return jsonify(students)

@todo.route('/student/get/<int:id>',methods=['GET'])
def student_id( id ):
    student=next((student for student in students if student['id']==id),None)

    if student is None:
        return jsonify({'message':'student not found'}),404

    return jsonify(student)


if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True

    )