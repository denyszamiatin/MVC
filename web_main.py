from flask import Flask, render_template, request, redirect, g, session
import redis_contacts
import dummy_serializer


app = Flask(__name__)
app.secret_key = 'icowicopwe3t 21p3o23p[asdpkl-'


@app.before_request
def before_request():
    g.r = redis_contacts.Contacts(dummy_serializer.Serializer())


@app.route('/')
def index():
    message = session.pop('message', '')
    contacts = g.r.read_all()
    return render_template('index.html', name='Bill', contacts=contacts, message=message)


@app.route('/add', methods=['GET', 'POST'])
def add():
    name = phone = message = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
        phone = request.form.get('phone', '')
        if name and phone:
            try:
                g.r.create_contact(name, phone)
            except ValueError as e:
                message = str(e)
            else:
                session['message'] = 'Contact has been added successfully'
                return redirect('/')
    return render_template('add.html', name=name, phone=phone, message=message)

if __name__ == '__main__':
    app.run(debug=True)