from flask import render_template
from app import app, db 


@app.errorhandler(404)
def not_found(error):
    return render_template('404error.html'), 404 


@app.errorhandler(500)
def internal_server(error):
    db.session.rollback()
    return render_template('500error.html'), 500 



####STATUS CODE TABLE
# 1XX --- info 
# 2XX --- Success
# 3XX --- redirect 
# 4XX --- Client errors 
# 5XX --- Server Error