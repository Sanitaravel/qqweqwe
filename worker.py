class Worker:
    def __init__(self, salary):
        self.salary = salary

    def payment(self, N):
        return self.salary * N
    
    def taxes(self, N):
        return self.salary * N * 0.13

def main():
    salary = int(input("Input your salary: "))
    N = int(input("Input how many days do you work: "))
    worker = Worker(salary)
    print(f'Your salary for {N} days of work would be {worker.payment(N)}.')
    print(f'You need to pay {worker.taxes(N)} in terms of taxes for {N} days.')

if __name__ == "__main__":
    main()