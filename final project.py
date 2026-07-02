Patients = []
def add_patient():
    print("Add New Patient")
    patient_id= len(Patients) + 1
    name = input ("Enter Patient name:").strip().title()
    try:
        age = int(input("Enter age:"))
    except ValueError:
        print ("Invalid age, Please enter a number.")
        return
    phone = input("Enter phone number: ").strip()
    symptoms = input("Enter symptoms: ").strip()

    patient = {"id": patient_id, "name": name, "age": age,"phone": phone,  "symptoms": symptoms,"visits" :[]}
    Patients.append(patient)
    print(f"Patient {name} added successfully!")
def view_patients():
    if not Patients:
        print("No recoreded patient")
        return

    print("Patient list")

    for patient in Patients:
        print(f"ID: {patient['id']}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Phone: {patient['phone']}")
        print(f"symptoms: {patient['symptoms']}")
        print("-" * 20) 

def search_patient():
    if not Patients:
        print("No patients in the system to search.")
        return

    name_to_search = input("Enter the name of the patient to search for: ").strip().title()
    found = False
    
    for patient in Patients:
        if patient['name'] == name_to_search:
            print("Patient Found:")
            print(f"ID: {patient['id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Phone: {patient['phone']}")
            print(f"Symptoms: {patient['symptoms']}")
            print("-" * 20)
            found = True
            break
            
    if not found:
        print(f"No patient found with the name '{name_to_search}'.")

def update_patient():
    patient_id = int(input("Enter patient ID to update: "))
    for patient in Patients:
        if patient['id'] == patient_id:
            print("What do you want to update? 1. Name 2. Age 3. Phone 4. Symptoms")
            choice = input("Choose an option: ")
            if choice == "1":
                patient['name'] = input("Enter new name: ").strip().title()
            elif choice == "2":
                patient['age'] = int(input("Enter new age: "))
            elif choice == "3":
                patient['phone'] = input("Enter new phone: ")
            elif choice == "4":
                patient['symptoms'] = input("Enter new symptoms: ")
            print("Patient updated successfully.")
            return
    print("Patient not found.")

def add_visit_note():
    patient_id = int(input("Enter patient ID: "))
    for patient in Patients:
        if patient['id'] == patient_id:
            date = input("Enter visit date: ")
            doctor = input("Enter doctor name: ")
            note = input("Enter visit note: ")
            advice = input("Enter prescription/advice: ")
            visit = {"date": date, "doctor": doctor, "note": note, "advice": advice}
            patient['visits'].append(visit)
            print("Visit note added successfully.")
            return
    print("Patient not found.")

def view_patient_history():
    if not Patients:
        print("No patients in the system to view history.")
        return

    try:
        patient_id = int(input("Enter patient ID to view history: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    found = False
    for patient in Patients:
        if patient['id'] == patient_id:
            found = True
            print(f"\nPatient: {patient['name']}")
            
            if not patient['visits']:
                print("No visit history found for this patient.")
            else:
                print("====== Visit History ======")
                for index, visit in enumerate(patient['visits'], start=1):
                    print(f"Visit {index}:")
                    print(f"  Date: {visit['date']}")
                    print(f"  Doctor: {visit['doctor']}")
                    print(f"  Note: {visit['note']}")
                    print(f"  Advice: {visit['advice']}")
                    print("-" * 20)
            break

    if not found:
        print(f"No patient found with ID {patient_id}.")

def save_data():
    with open("patients.json", "w") as file:
        json.dump(Patients, file, indent=4)
    print("Data saved successfully.")

def show_menu():
    print("Clincal Patient Management System")
    print("1. Add new Patient")
    print("2.View all Patients")
    print("3.Search Patient")
    print("4.Update patient information") 
    print("5.Add a visit or appointment note")
    print("6.Show patient history") 
    print("7.Save data to a file") 
    print("8.exit")


def main():
    while True: 
        show_menu()
        choice = input("choose an option:")
        if choice == "1":
            add_patient()
        elif choice =="2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            add_visit_note ()
        elif choice == "6":
            view_patient_history ()
        elif choice == "7":
            save_data ()
        elif choice == "8":
            save_data ()
            print("Thank you for using the system , Goodbye !")
            break
        else: 
            print("InValid choice, please try again.")
main()