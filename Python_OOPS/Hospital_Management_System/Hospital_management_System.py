class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Patient(Person):
    def __init__(self, name, age, gender, patient_id, ailment):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.ailment = ailment

    def display_details(self):
        super().display_details()
        print(f"Patient ID: {self.patient_id}, Ailment: {self.ailment}")


class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_details(self):
        super().display_details()
        print(f"Doctor ID: {self.doctor_id}, Specialization: {self.specialization}")


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added successfully.")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added successfully.")

    def display_patients(self):
        print("Patients List:")
        for patient in self.patients:
            patient.display_details()

    def display_doctors(self):
        print("Doctors List:")
        for doctor in self.doctors:
            doctor.display_details()


# Example Usage
if __name__ == "__main__":
    hospital = Hospital("City Hospital")

    # Adding Patients
    patient1 = Patient("Alice", 30, "Female", "P001", "Fever")
    patient2 = Patient("Bob", 45, "Male", "P002", "Diabetes")
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    # Adding Doctors
    doctor1 = Doctor("Dr. Smith", 50, "Male", "D001", "Cardiology")
    doctor2 = Doctor("Dr. Jane", 40, "Female", "D002", "Neurology")
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)

    # Displaying Details
    hospital.display_patients()
    hospital.display_doctors()