
from flask import Flask, request, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

students = {
    1: {"name": "John Doe", "age": 20, "grade": "A"},
    2: {"name": "Jane Smith", "age": 22, "grade": "B"},
    3: {"name": "Bob Johnson", "age": 21, "grade": "C"},
}


class Student(Resource):
    def get(self, student_id):
        return students[student_id]

    def put(self, student_id):
        data = request.get_json()
        students[student_id] = data
        return {"message": "Student record updated", "student_id": student_id}


api.add_resource(Student, "/student/<int:student_id>")


@app.route('/')
def home_page():
    # Create an HTML representation of the students' data
    student_list_html = "<h2>Student Data:</h2><ul>"
    for student_id, student_info in students.items():
        student_list_html += f"<li>Student ID: {student_id}, Name: {student_info['name']}, Age: {student_info['age']}, Grade: {student_info['grade']}</li>"
    student_list_html += "</ul>"

    return f"<html><body>Welcome to the Student API!<br>{student_list_html}</body></html>"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

