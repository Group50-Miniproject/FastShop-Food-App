from fastshop.routes import app
from fastshop import db

@app.before_first_request
def create_tables():
    db.create_all()

#checks if main.py has executed directly and not imported
if __name__ == '__main__':
    app.run(debug = True)


