# people.py
from flask import abort,make_response

from config import db
from models import Person, people_schema, person_schema


def read_all():
    people = Person.query.all()
    return people_schema.dump(people)

def create(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        #db.session.close()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with last name {lname} already exists")

def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")

def update(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        #db.session.close()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")

def delete(lname):
    #  with app.app_context():
    #     person = Person.query.get(person_id)
    #     if person is None:
    #         return jsonify({'error': 'Person not found'}), 404
    #     db.session.delete(person)
    #     db.session.commit()
    #     db.session.close()  # close the database session
    #     return jsonify({'success': 'Person deleted'})

    
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()
    print(person_schema.dump(existing_person).get('lname'))
    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        #db.session.close()
        return make_response(f"{lname} successfully deleted", 204)
    else:
        abort(404, f"Person with last name {lname} not found")