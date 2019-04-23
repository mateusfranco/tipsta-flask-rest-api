from datetime import date

from app import db

class Event(models.Model): 
    name_event = models.CharField(max_length=50)
    event_location = models.CharField(max_length=50)
    coverage_area = models.CharField(max_length=50)
    date_start_event = models.DateField(auto_now=False, auto_now_add=False)
    date_end_event = models.DateField(auto_now=False, auto_now_add=False)
    event_deion = models.TextField()
    event_coordinator = models.OneToOneField(User, on_delete=models.CASCADE)

    def __repr__(self):
        return '<>Evento: {}'.format(self.name_event)

