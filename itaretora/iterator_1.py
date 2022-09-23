# iterators

class Test:

    def __init__(self, limit):
        self.limit = limit

    # Creates iterator object
    def __iter__(self):
        self.x = 10
        return self


    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        self.x = x + 1;
        return x


#  numbers from 10 to 15
for i in Test(15):
    print(i)

for i in Test(5):
    print(i)