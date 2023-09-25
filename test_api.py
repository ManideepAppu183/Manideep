import requests

BASE_URL = "http://127.0.0.1:5000/"
student_data = {"name": "Jhonny", "age": 23, "grade": "A"}

student_id = 1

response = requests.put(BASE_URL + f"student/{student_id}", json=student_data)

if response.status_code == 200:
    print("Student record updated successfully.")
    print(response.json())
else:
    print("Failed to update student record.")
    print(response.status_code, response.json())
