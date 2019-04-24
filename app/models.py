from datetime import date

from app import db
class Event(db.Model): 
    """
    Create an Event table
    """
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    name_event = db.Column(db.String(256))
    event_location = db.Column(db.String(512))
    coverage_area = db.Column(db.String(64))
    date_start_event = db.Column(db.Date)
    date_end_event = db.Column(db.Date)
    event_description = db.Column(db.String(2048))
    event_coordinator = db.Column(db.Integer, nullable=False) 
    #event_coordinator = models.OneToOneField(User, on_delete=models.CASCADE) << Criar chave Foreign key 

    def __repr__(self):
        return '<>Evento: {}'.format(self.name_event)
