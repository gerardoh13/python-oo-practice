"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """initializes serial number with given starting value"""
        self.start = start
        self.next = start + 1

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """returns an int starting with the starting number, and increases it by 1 everytime it is called"""
        self.next += 1
        return self.next - 2


    def reset(self):
        """resets the returned number returned by generate() back to the starting number"""
        self.next = self.start + 1


