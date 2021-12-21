# https://github.com/terror/kattis-api

import kattis

username = ""
password = ""

user = kattis.auth(username, password)

problems = user.problems(1)
stats = user.stats()
info = user.data()
