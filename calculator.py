
class Calculator:

    last_res = None

    def sum(self, n1, n2):
        self.last_res = n1 + n2
        return self.last_res

    def print_last_res(self):
        print(self.last_res)

    def division(self, n1, n2):
        try:
            self.last_res = n1/n2
        except:
            pass
        return self.last_res