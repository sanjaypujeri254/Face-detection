import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("pythonproject-f8690-firebase-adminsdk-i0cwe-98dd801587.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://pythonproject-f8690-default-rtdb.firebaseio.com/",
    # 'storageBucket': ""
})
ref = db.reference('Students')

data = {
    "21ABC001":
        {
            "name": "ABC",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "Performance": "Good",
            "year": 3,
            "last_attendance_time": "2024-05-01 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
