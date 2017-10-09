students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in range(0, len(students)):
    print "{} {}".format(students[i]["first_name"], students[i]["last_name"])


users = {
    "Students": [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    "Instructors": [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}

for group in users:
    print group
    group_of_users = users[group]
    # print group_of_users
    for i in range(0, len(group_of_users)):
        full_name = group_of_users[i]["first_name"] + group_of_users[i]["last_name"]
        print "{} - {} {} - {}".format(i+1, group_of_users[i]["first_name"], group_of_users[i]["last_name"], len(full_name))
