from flask import Flask,render_template


FOI=Flask(__name__)

@FOI.route('/wish')   #Routing is nothing but URl Mapping in django
def wish():
    return 'Always King ........! '

@FOI.route('/page')
def page():
    return render_template('page.html',name='King',age=99)   #Returning of Html Page ,Context also provede here only

FOI.run(debug=True)