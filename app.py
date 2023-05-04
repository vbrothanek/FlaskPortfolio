from flask import Flask, render_template, request
from generator import Generator

app = Flask(__name__)

dict_of_used_characters = {
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
    '''
    The /generate page generates a password according to the user input. 
    If a request is sent by the GET method, the /generate html page is sent and the first password is generated based on the default values. 
    If the request is sent by POST method, the password is generated based on the user input in the fomrular on the HTML page
    '''
    if request.method == 'GET':
        char_to_passwd = Generator(
            capital_letters = dict_of_used_characters['capital_letters'],
            letters = dict_of_used_characters['letters'],
            numbers = dict_of_used_characters['numbers'],
            symbols = dict_of_used_characters['symbols'])
        
        generated_password = char_to_passwd.generated_password(lenght=dict_of_used_characters['lenght'])
        return render_template("generovat.html", generated_password=generated_password)
    
    elif request.method == 'POST':
        char_to_passwd = Generator(
            capital_letters = dict_of_used_characters['capital_letters'],
            letters = dict_of_used_characters['letters'],
            numbers = dict_of_used_characters['numbers'],
            symbols = dict_of_used_characters['symbols'])
        
        
        lenght = int(request.form.get('lenght'))
        capital_letters = request.form.get('capital_letters')
        letters = request.form.get('letters')
        numbers = request.form.get('numbers')
        symbols = request.form.get('symbols')
        dict_of_used_characters.update(
            {
                'lenght': lenght,
                'capital_letters': capital_letters, 
                'letters': letters, 
                'numbers': numbers, 
                'symbols': symbols
                }
        )
        
        generated_password = char_to_passwd.generated_password(lenght=dict_of_used_characters['lenght'])
        return render_template("generovat.html", generated_password=generated_password)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
    # app.run(debug=True, host='0.0.0.0', port=5001)
    # print(get_requirments_of_password['lenght'])
    # print(get_requirments_of_password['symbols'])