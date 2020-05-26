'''
Observer
	- Establishes a one-to-many relationship between a subject and multiple observers
	- Problem:
		+ Subjects need to be monitored for a changes, then observers need to be notified
	- Useful Case(s)
		+ Database in server is being monitored during week day games so stats need to be
		  notified and changed dynamically
'''


class Subject(object):  # Represents what is being 'observed'

    def __init__(self):
        self._observers = []  # This where references to all the observers are being kept
        # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):  # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Table(Subject):  # Inherits from the Subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # Set the name of the core
        self._stat = str()  # Initialize the stat in the table

    @property  # Getter that gets the table stat
    def stat(self):
        return self._stat

    @stat.setter  # Setter that sets the table stat
    def stat(self, stat):
        self._stat = stat
        self.notify()


class StatViewer:

    def update(self, subject):  # Alert method that is invoked when the notify() method in a concrete subject is invoked
        print("Statistic Viewer: '{}' has stat '{}'".format(
            subject._name, subject._stat))


# Let's create our subjects
table1 = Table("Traditional")
table2 = Table("Advanced")

# Let's create our observers
v1 = StatViewer()
v2 = StatViewer()

# Let's attach our observers to the first table
table1.attach(v1)
table1.attach(v2)

# Let's change the stat of our first table
table1.stat = "pts"
table1.stat = "pie"
