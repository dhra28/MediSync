class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def get_details(self):
        return f"{self.name} ({self.age}) - {self.disease}"

if __name__ == "__main__":
    p1 = Patient("Alice", 30, "Flu")
    p2 = Patient("Bob", 50, "Hypertension")

    print(p1.get_details())
    print(p2.get_details())