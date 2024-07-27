import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("face-detection-3fe8d-firebase-adminsdk-bcfy7-78e44dc191.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-detection-3fe8d-default-rtdb.firebaseio.com/",
    # 'storageBucket': ""
})
ref = db.reference('Students')

data = {
    "2JR21CS083":
        {
            "name": "Sanjay Pujeri",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "Performance": "Good",
            "year": 3,
            "last_attendance_time": "2024-05-01 00:54:34"
        },
    "2JR21CS090":
        {
            "name": "Shreehari K",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "Performance": "Good",
            "year": 3,
            "last_attendance_time": "2024-05-01 00:54:34"
        },
    "2JR21CS096":
        {
            "name": "Sneha S",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "Performance": "Good",
            "year": 3,
            "last_attendance_time": "2024-05-01 00:54:34"
        },
    "2JR21CS410":
        {
            "name": "Ruchita K",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "Performance": "Good",
            "year": 3,
            "last_attendance_time": "2024-05-01 00:54:34"
        },
"2JR21CS411":
        {
            "name": "abc",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "Performance": "Good",
            "year": 3,
            "last_attendance_time": "2024-05-01 00:54:34"
        },
"2JR21CS412":
        {
            "name": "xyz",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "Performance": "Good",
            "year": 3,
            "last_attendance_time": "2024-05-01 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
