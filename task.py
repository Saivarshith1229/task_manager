from datetime import datetime

class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} - {self.description}" 