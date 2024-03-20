from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    ''' 
    opens the response.html and replace the context variable with you are in homepage
    '''
    return render_template('response.html',context="you are in homepage")

@app.route('/view',methods=['GET'])
def view():
    ''' 
    opens the response.html and replace the context variable with you are in viewpage
    '''
    return render_template('response.html',context='You are in viewPage')

@app.route('/add',methods=['GET'])
def addition():
    ''' 
    opens the form.html and 
    replace the path variable with /addition-form and
    form_name variable with Addition form
    '''
    return render_template('form.html',path="/addition-form",form_name='Addition form')

@app.route('/addition-form',methods=['POST'])
def addition_form():
    '''
    receives the form data from form.html and storing in the num1 and num2 variables
    addition of those two variables will be stored in result variable
    and opens the response.html where context variable will be replaced by result
    '''
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    num1 = int(num1)
    num2 = int(num2)
    result = f"addition of {num1} and {num2} is {num1+num2}"
    return render_template('response.html',context=result)

@app.route('/sub',methods=['GET'])
def subtraction():
    ''' 
    opens the form.html and 
    replace the path variable with /subtraction-form and
    form_name variable with Subtraction form
    '''
    return render_template('form.html',path="/subtraction-form",form_name='Subtraction form')

@app.route('/subtraction-form',methods=['POST'])
def subtraction_form():
    '''
    receives the form data from form.html and storing in the num1 and num2 variables
    subtraction of those two variables will be stored in result variable
    and opens the response.html where context variable will be replaced by result
    '''
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    num1 = int(num1)
    num2 = int(num2)
    result = f"subtraction of {num1} and {num2} is {abs(num1-num2)}"
    return render_template('response.html',context=result)

@app.route('/mul',methods=['GET'])
def multiplication():
    ''' 
    opens the form.html and 
    replace the path variable with /multiplication-form and
    form_name variable with Multiplication form
    '''
    return render_template('form.html',path="/multiplication-form",form_name='Multiplication form')

@app.route('/multiplication-form',methods=['POST'])
def multiplication_form():
    '''
    receives the form data from form.html and storing in the num1 and num2 variables
    multiplication of those two variables will be stored in result variable
    and opens the response.html where context variable will be replaced by result
    '''
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    num1 = int(num1)
    num2 = int(num2)
    result = f"multiplication of {num1} and {num2} is {num1*num2}"
    return render_template('response.html',context=result)

@app.route('/div',methods=['GET'])
def division():
    ''' 
    opens the form.html and 
    replace the path variable with /division-form and
    form_name variable with Division form
    '''
    return render_template('form.html',path="/division-form",form_name='Division form')

@app.route('/division-form',methods=['POST'])
def division_form():
    '''
    receives the form data from form.html and storing in the num1 and num2 variables
    division of those two variables will be stored in result variable
    and opens the response.html where context variable will be replaced by result
    '''
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    num1 = int(num1)
    num2 = int(num2)
    result = f"division of {num1} and {num2} is {num1/num2}"
    return render_template('response.html',context=result)