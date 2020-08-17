"""Single Responsibility Principle"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, position):
        del self.entries[position]

    """Display the data in a human readable form"""
    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I woke up happy today')
j.add_entry('Human brain is a separate organism')
j.add_entry('The human brain is trying to go out in space to reach the planet it came from {=_=} ')
# print(f'Journal entries: \n{j}')

file = r'C:\Users\rajeevs\Documents\python_design_patterns\temp.txt'
PersistenceManager.save_to_file(j, file)

# Verifying the journal
with open(file) as fh:
    print(fh.read())