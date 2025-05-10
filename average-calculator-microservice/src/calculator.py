class Calculator:
    def __init__(self,max_window_size):
        self.max_window_size=max_window_size
        self.numbers=[]
        
#Upon breaching the window size, replace the oldest number with the newest one.
    def add_number(self, number):
        if len(self.numbers)>=self.max_window_size:
            self.numbers.pop(0) 
        self.numbers.append(number)

#Calculating the average of the numbers in the list.
    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def get_numbers(self):
        return self.numbers.copy()