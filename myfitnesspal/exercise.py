class Exercise():
    def __init__(self, burnedCalories):
        self._burnedCalories = burnedCalories

    @property
    def burnedCalories(self):
        if(self._burnedCalories == None):
            return "0"
        else:
            return self._burnedCalories

