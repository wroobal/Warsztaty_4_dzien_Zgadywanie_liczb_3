from flask import Flask
from flask import request

app = Flask(__name__)

BLABLA = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess the number</title>
    </head><body><h1><center>IMAGINE NUMBER 1-1000</center></h1>
    <form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <center><input type="submit" value="OK"></center></input>
    </form></body></html>
"""
BLABLA2 = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head><body><h1>It is number {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="To big">
    <input type="submit" name="user_answer" value="To small">
    <input type="submit" name="user_answer" value="You win">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form></body></html>
"""
BLABLA3 = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body><h1>I guess! Your number is {guess}</h1></body>
</html>
"""

@app.route('/', methods=['GET','POST'])
def guessing():
    if request.method == 'GET':
        return BLABLA.format(0,1000)
    else:
        min = int(request.form.get('min'))
        max = int(request.form.get('max'))
        answer = request.form.get('user_answer')
        guess = int(request.form.get('guess', 500))
        if answer == 'To big':
            max = guess
        elif answer == 'To small':
            min = guess
        elif answer == 'You win':
            return BLABLA3.format(guess=guess)

        guess = int((max - min)/2) + min

        return BLABLA2.format(guess=guess, min=min, max=max)
if __name__ == "__main__":
    app.run(debug=True)


