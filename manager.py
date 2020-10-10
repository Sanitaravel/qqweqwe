class Worker:
    def __init__(self, salary = 100):
        self.salary = salary

    def payment(self, N):
        return self.salary * N
    
    def taxes(self, N):
        return self.salary * N * 0.13


class Manager(Worker):
    def __init__(self, salary = 100):
        Worker.__init__(self, salary)
        self.extras = self.salary * 0.36
    
    def payment(self, N):
        return Worker.payment(self, N) + self.extras * N


def main():
    salary = int(input("Input your salary: "))
    N = int(input("Input how many days do you work: "))
    manager = Manager(salary)
    print(f'Your salary for {N} days of work would be {manager.payment(N)}.')
    print(f'You need to pay {manager.taxes(N)} in terms of taxes for {N} days.')

if __name__ == "__main__":
    main()