from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/lyrics', methods=['GET', 'POST'])
@app.route('/lyrics.html', methods=['GET', 'POST'])
def lyrics():
    madlibs = request.form.to_dict()
    (street,animal,verb,clothing,clothing_plural,color,vehicle, place,plural_animal,people) = model.process_data(madlibs)
    
    return render_template('lyrics.html', street=street, animal=animal, verb=verb, clothing=clothing, clothing_plural=clothing_plural, color=color, vehicle=vehicle,place=place, plural_animal=plural_animal, people=people)
