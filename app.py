from flask import Flask, render_template, request
from generator import Generator

app = Flask(__name__)

get_requirments_of_password = {
    'lenght': 8,
    'capital_letters': True, 
    'letters': True, 
    'numbers': True, 
    'symbols': False
}


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/generovat', methods=['GET', 'POST'])
def generator():
    if request.method == 'GET':
        generate = Generator(
            capital_letters = get_requirments_of_password['capital_letters'],
            letters = get_requirments_of_password['letters'],
            numbers = get_requirments_of_password['numbers'],
            symbols = get_requirments_of_password['symbols'])
        return render_template("generovat.html", generated_password=generate.generated_password(lenght=get_requirments_of_password['lenght']))
    
    elif request.method == 'POST':
        lenght = int(request.form.get('lenght'))
        capital_letters = request.form.get('capital_letters')
        letters = request.form.get('letters')
        numbers = request.form.get('numbers')
        symbols = request.form.get('symbols')
        get_requirments_of_password.update(
            {
                'lenght': lenght,
                'capital_letters': capital_letters, 
                'letters': letters, 
                'numbers': numbers, 
                'symbols': symbols
                }
        )
        generate = Generator(
            capital_letters = get_requirments_of_password['capital_letters'],
            letters = get_requirments_of_password['letters'],
            numbers = get_requirments_of_password['numbers'],
            symbols = get_requirments_of_password['symbols'])
        return render_template("generovat.html", generated_password=generate.generated_password(lenght=get_requirments_of_password['lenght']))



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0', port=5001)
    # print(get_requirments_of_password['lenght'])
    # print(get_requirments_of_password['symbols'])