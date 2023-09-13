
from tabulate import tabulate
import csv

#  sampel 
employees = []

# menunjukkan data karyawan
def display_employee_data():
    if not employees:
        print("Data karyawan tidak tersedia.")
        return

headers = ["nama lengkap", "ID", "jabatan", "tanggal mulai kerja", "performa"]
data = [
    {"nama lengkap": 'andri e sandi', "ID": 340402, "jabatan": 'supervisor', "tanggal mulai kerja": '2020-11-9', "performa": 'sangat bagus'},
    {"nama lengkap": 'laura amadea', "ID": 340403, "jabatan": 'karyawan admin', "tanggal mulai kerja": '2022-10-12', "performa": 'bagus'},
    {"nama lengkap": 'pongky barata', "ID": 340404, "jabatan": 'karyawan marketing', "tanggal mulai kerja": '2023-5-23', "performa": 'sangat buruk'},
    {"nama lengkap": 'Bodi aswanata', "ID": 340405, "jabatan": 'karyawan marketing', "tanggal mulai kerja": '2021-9-9', "performa": 'sangat bagus'},
    {"nama lengkap": 'Rian Prahasmara', "ID": 340406, "jabatan": 'karyawan IT', "tanggal mulai kerja": '2021-11-28', "performa": 'biasa'} 
    ]
    
path = 'karyawan.csv'

with open(path, 'w', newline='') as file:
    exampleWriter = csv.DictWriter(file, fieldnames=headers, delimiter=';')
    exampleWriter.writeheader()
    exampleWriter.writerows(data)


with open(path, 'r') as file:
    exampleReader = csv.reader(file, delimiter=";")
    for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

print(tabulate(data, headers, tablefmt="fancy_grid"))
print (display_employee_data)

# menambah karyawan
def create_employee():
    full_name = input("masukkan nama lengkap: ")
    emp_id = int(input("masukkan nomor ID: "))
    position = input("masukkan jabatan: ")
    hiring_date = input("masukkan tanggal kerja (YYYY-MM-DD): ")
    performance = input("masukkan hasil performa: ")
    
    for employee in employees:
        if employee["ID"] == emp_id:
            print("data karyawan sudah ada.")
            return

    employee = {
        "nama lengkap": full_name,
        "ID": emp_id,
        "jabatan": position,
        "tanggal mulai kerja": hiring_date,
        "performa": performance,
    }

    employees.append(employee)
    print("data karyawan berhasil dibuat.")
    print(tabulate([employee.values()], headers=employee.keys(), tablefmt="fancy_grid"))

    save_decision = input("Apakah Anda ingin menyimpan data baru? (yes/no): ")
    if save_decision.lower() == "yes":
        employees.append(employee)
        print("Data karyawan berhasil disimpan.")
    else:
        print("Data karyawan tidak disimpan.")


# fungsi update karyawan
def update_employee():
    emp_id = int(input("masukkan id: "))
    for emp in employees:
        if emp["ID"] == emp_id:
            print("temukan karyawan:")
            print(tabulate([emp.values()], headers=emp.keys(), tablefmt="fancy_grid"))

            field_to_update = input("Bagian intuk di update (nama lengkap/jabatan/tanggal mulai kerja/peforma): ").strip()
            new_value = input(f"Enter the new value for {field_to_update}: ")

            if field_to_update in emp:
                emp[field_to_update] = new_value
                print("data karyawan berhasil ditambah.")
                return

    print("data karyawan tidak ada.")

# fungsi menghapus karyawan
def delete_employee():
    emp_id = int(input("masukkan ID karyawan yang mau dihapus: "))
    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            print("data karyawan berhasil dihapus.")
            return

    print("ID karyawan tidak ditemukan.")

#klasifikasi karyawan
def Classify_employee():
    emp= str(input("masukkan performa karyawan: "))
    if emp== "sangat buruk":
        print (" ajukan ke HRD")
    elif emp== "biasa":
        print ("naikkan kualitas")
    elif emp== "bagus":
        print  ("pertahankan")
    elif emp== "sangat bagus":   
        print  ("rekomendasi naik jabatan")
    else:
        print ("klasifikasi tidak ada")

# Main menu
def main_menu():
    while True:
        print("\nEmployee Data Management")
        print("1. tunjukkan data karyawan")
        print("2. buat data karyawan")
        print("3. update data karyawan")
        print("4. hapus karyawan")
        print("5. performa karyawan")
        print("6.exit")

        choice = input("pilih opsi yang diinginkan: ")

        if choice == "1":
            display_employee_data()
        elif choice == "2":
            create_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "6":
            print("selesai. terima kasih!")
        elif choice== "5":
            Classify_employee()
        else:
            print("pilihan tidak ada. harap diulang.")


if __name__ == "__main__":
    main_menu()
    #selesai bro.....
