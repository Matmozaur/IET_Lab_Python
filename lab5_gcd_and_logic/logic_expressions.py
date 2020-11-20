class LogicAutomat:

    def __init__(self):
        self.state = 'q0'
        self.counter = 0

    def reset(self):
        self.__init__() # sugeruję odwrotnie - __init__ niech wywoła reset

    def handle_expression(self, expression):
        expression = expression.replace(" ", "")
        for c in expression:
            self.next_step(c)
            if self.counter < 0 or self.state == 'qN':
                return False
        if self.state == 'q1' and self.counter == 0:
            return True
        else:
            return False

    def next_step(self, c):
        if self.state == 'q0':
            self.next_step_q0(c)
        else:
            self.next_step_q1(c)    # jeśli już Pan to robi tak uniwerslanie, to sugeruję słownik

    def next_step_q0(self, c):
        if c == '(':
            self.counter += 1
        elif c == '~':
            pass
        elif c.islower() and ord(c) < 128:  # a stałe?
            self.state = 'q1'
        else:
            self.state = 'qN'

    def next_step_q1(self, c):
        if c == ')':
            self.counter -= 1   # właściwie sprawdzenie countera mogłoby być tutaj
        elif c in {'&', '|'}:
            self.state = 'q0'
        else:
            self.state = 'qN'


def evaluate_expression(expresion):
    automat = LogicAutomat()
    is_valid = automat.handle_expression(expresion)
    automat.reset() # po co, skoro za chwilę tego automatu nie będzie?
    return is_valid


if __name__ == '__main__':
    ex1 = 'a&b&~(~a|c)'
    print(evaluate_expression(ex1))
    ex2 = 'aa&b&~(~a|c)'
    print(evaluate_expression(ex2))
    ex3 = 'a)|b&~(~a|c)'
    print(evaluate_expression(ex3))
    ex4 = 'a&(b&~(~a|c)'
    print(evaluate_expression(ex4))
