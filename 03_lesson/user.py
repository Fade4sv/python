class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def f_name(self):
        return self.fname

    def l_name(self):
        return self.lname

    def fio(self):
        return f"{self.fname} {self.lname}"


