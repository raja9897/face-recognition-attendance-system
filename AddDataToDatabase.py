import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-9d7fa-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')


data = {
    "1001":
        {
            "name": "Mark Zuckerberg",
            "major": "Robotics",
            "starting_year": 2018,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",



        },
    "1002":
        {
            "name": "girl",
            "major": "Robotics",
            "starting_year": 2018,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",

        },
    "1003":
        {
            "name": "Elon",
            "major": "Robotics",
            "starting_year": 2018,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",

        },
    "1004":
        {
            "name": "Raja Babu",
            "major": "Robotics",
            "starting_year": 2018,
            "total_attendance": 1,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",

        },
    "1005":
        {
            "name": "sharukhan",
            "major": "Robotics",
            "starting_year": 2018,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",

        },
    "1006":
        {
            "name": "Jagendra Singh",
            "major": "Rob",
            "starting_year": 2018,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",

        }
}

for key,value in data.items():
    ref.child(key).set(value)