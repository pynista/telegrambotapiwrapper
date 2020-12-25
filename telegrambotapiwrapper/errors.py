class Error(Exception):
    pass


class UnsuccessfulRequest(Error):

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        if hasattr(self, 'parameters'):
            return f"{self.__class__.__name__}(description='{self.description}', error_code='{self.error_code}', parameters={self.parameters}"
        else:
            return f"{self.__class__.__name__}(description='{self.description}', error_code='{self.error_code}'"

    def __str__(self):
        if hasattr(self, 'parameters'):
            return f"\ndescription='{self.description}'\nerror_code='{self.error_code}'\nparameters={self.parameters}"
        else:
            return f"(description='{self.description}', error_code='{self.error_code}')"
