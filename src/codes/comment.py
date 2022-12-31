from codes.basecode import Command

COMMENT_CHAR = '#'

class Comment(Command):
    
    def __init__(self, line):
        super().__init__(line)
        
    def run(self):
        return True
    
    def get_data(self):
        return None
    