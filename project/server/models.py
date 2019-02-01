# project/server/models.py
from project.server import db, marshmallow

class Accident(db.Model):

    __tablename__ = "caracteristiques"

    num_acc = db.Column('num_acc', db.Integer(), primary_key=True)
    lum = db.Column('lum', db.Integer())
    agg = db.Column('agg', db.Integer())
    int = db.Column('int', db.Integer())
    atm = db.Column('atm', db.Integer())
    col = db.Column('col', db.Integer())
    adr = db.Column('adr', db.Text())
    comm = db.Column('comm', db.String(5))
    gps = db.Column('gps', db.String(1))
    dep = db.Column('dep', db.String(3))
    lat = db.Column('lat', db.Float())
    long = db.Column('long', db.Float())
    date = db.Column('date', db.DateTime())

    def __init__(self, num_acc, lum, agg, int, atm, col,
                 adr, comm, gps, dep, lat, long, date):
        self.num_acc = num_acc
        self.lum = lum
        self.agg = agg
        self.int = int
        self.atm = atm
        self.col = col
        self.adr = adr
        self.comm = comm
        self.gps = gps
        self.dep = dep
        self.lat = lat
        self.long = long
        self.date = date

    def __repr__(self):
        return '<Accident {0} >'.format(self.num_acc)


class AccidentSchema(marshmallow.ModelSchema):
    class Meta:
        fields = ('num_acc', 'lum', 'agg', 'int', 'atm', 'adr', 'col',
                  'comm', 'gps', 'dep', 'lat', 'long', 'date')
        ordered = True
        model = Accident


accident_schema = AccidentSchema()
accidents_schema = AccidentSchema(many=True)
