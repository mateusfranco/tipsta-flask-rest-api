from datetime import date

from app import db
class Event(db.Model): 
    """
    Create a Event table
    """
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    location = db.Column(db.String(512))
    coverage_area = db.Column(db.String(64))
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    description = db.Column(db.String(2048))
    coordinator = db.Column(db.Integer, nullable=False)
    accepted = db.Column(db.Boolean, unique=False, default=False) 
    trail = db.relationship('Trail', backref='events', cascade='all, delete-orphan', lazy='dynamic')
    
    def __repr__(self):
        return '<>Evento: {}'.format(self.name)

class Trail(db.Model):
    """
    Create a Trail table
    """
    __tablename__ = 'trail'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    description = db.Column(db.String(2048))
    date_start = db.Column(db.Date)
    date_end = db.Column(db.Date)
    coordinator = db.Column(db.Integer)
    belong = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    checklist = db.relationship('Checklist', backref='trail', cascade='all, delete-orphan', lazy='dynamic')
    appraiser = db.relationship('Appraiser', backref='trail', cascade='all, delete-orphan', lazy='dynamic')
    submission = db.relationship('Submission', backref='trail', cascade='all, delete-orphan', lazy='dynamic')

    def __repr__(self):
        return '<>Trilha: {}'.format(self.name)

class Submission(db.Model):
    """
    Create a Submission table
    """
    __tablename__ = 'submission'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    description = db.Column(db.String(2048))
    file = db.Column(db.String(256))
    status = db.Column(db.String(64))
    grade = db.Column(db.Integer)
    author = db.Column(db.Integer)
    submitted = db.Column(db.Integer, db.ForeignKey('trail.id', nullable=False))

    def __repr__(self):
        return '<>Submissao: {}'.format(self.title)

class Checklist(db.Model):
    """
    Create a Checklist table
    """
    __tablename__ = 'checklist'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256))
    weight = db.Column(db.Integer)
    belong = db.Column(db.Integer, db.ForeignKey('trail.id'), nullable=False)

    def __repr__(self):
        return '<>Checklist: {}'.format(self.description)

class Appraiser(db.Model):
    """
    Create a Appraiser table
    """
    __tablename__ = 'appraiser'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    in_trail = db.Column(db.Integer, db.ForeignKey('trail.id'), nullable=False)
    appraise = db.relationship('Trail')

    #def __repr__(self):
    #   return '<>Checklist: {}'.format(self.description)
