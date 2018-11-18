#!/usr/bin/env python3

from vectorcloud import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.Text)

    def __repr__(self):
        return self.command


class Output(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    output = db.Column(db.Text)

    def __repr__(self):
        return self.output


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return self.username


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    script_name = db.Column(db.Text)
    description = db.Column(db.Text)
    icon = db.Column(db.String(20))
    hex_id = db.Column(db.Text)

    def __repr__(self):
        return [self.id, self.script_name, self.description, self.hex_id]


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Text)
    battery_voltage = db.Column(db.Float)
    battery_level = db.Column(db.Integer)
    status_charging = db.Column(db.Boolean)
    cube_battery_level = db.Column(db.Integer)
    cube_id = db.Column(db.Text)
    cube_battery_volts = db.Column(db.Float)

    def __repr__(self):
        return [self.id, self.battery_voltage, self.battery_level,
                self.status_charging, self.cube_battery_level,
                self.cube_id, self.cube_battery_volts]
