from flask import current_app
from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)
    goal = db.relationship('Goal', back_populates='tasks')

    def to_dict(self):
        if not self.completed_at:
             is_complete = False
        else:
             is_complete = True
        if not self.completed_at:
            task_dict = {
                "id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": False
                }
            if self.goal_id:
                task_dict["goal_id"] = self.goal_id
            return task_dict
            
        elif self.completed_at:
            return {
                "id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": True
            }
