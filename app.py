from flask import Flask, render_template

app =  Flask(__name__)


post =[
    {
    'author':'Shoffy0',
    'title':'komg kong',
    'content':'story'
     }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__== '__main__':
    app.run(debug=True)