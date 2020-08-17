from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
# print(__name__)


# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('./index1.html', name=username, post_id=post_id)

# @app.route('/')
# def hello_world():
#     return render_template('./index1.html')

@app.route('/blog')
def blog():
    return 'Hello, blog!'


@app.route('/')
def hello_home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'./{page_name}.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            # write_to_csv(data)
            # write_to_file(data)
            return redirect('/thank_you')
        except:
            return 'Something went wrong'

    else:
        return 'problem'
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
#
# @app.route('/works')
# def hello_work():
#     return render_template('./works.html')
#
#
# @app.route('/about')
# def hello_about():
#     return render_template('./about.html')
#
#
# @app.route('/contact')
# def hello_contact():
#     return render_template('./contact.html')
#
#
# @app.route('/components')
# def hello_components():
#     return render_template('./components.html')

