from app import db


class StudenMail(db.Model):
    __tablename__ = 'student_mail'

    mail_id = db.Column(db.Integer, primary_key=True)
    mail_domain = db.Column(db.String)
    university_name = db.Column(db.String)

    @classmethod
    def find_all(cls):
        return cls.query.all()
