from tabulate import tabulate
import random
import csv
import flask
import pyinputplus as pyip





# Sample data
data = [
    {"nama_lengkap": 'toni markus', "ID": 340402, "jabatan": 'supervisor', "tanggal_mulai_kerja": '2020-11-9', "performa": 'sangat bagus'},
    {"nama_lengkap": 'laura amadea', "ID": 340403, "jabatan": 'karyawan admin', "tanggal_mulai_kerja": '2022-10-12', "performa": 'bagus'},
    {"nama_lengkap": 'pongky barata', "ID": 340404, "jabatan": 'karyawan marketing', "tanggal_mulai_kerja": '2023-5-23', "performa": 'sangat buruk'},
    {"nama_lengkap": 'Bodi aswanata', "ID": 340405, "jabatan": 'karyawan marketing', "tanggal_mulai_kerja": '2021-9-9', "performa": 'sangat bagus'},
    {"nama_lengkap": 'Rian Prahasmara', "ID": 340406, "jabatan": 'karyawan IT', "tanggal_mulai_kerja": '2021-11-28', "performa": 'biasa'} 
]

# Menunjukkan data karyawan 
def display_employee_data():
    headers = ["nama_lengkap", "ID"]
    partial_data = [{key: employee[key] for key in headers} for employee in data]
    print(tabulate(partial_data, headers="keys", tablefmt="grid"))

    show_full_data = input("Apakah Anda ingin menampilkan seluruh data karyawan? (yes/no): ")
    if show_full_data.lower() == "yes":
        print(tabulate(data, headers="keys", tablefmt="grid"))


# Menambah karyawan
def create_employee():
    global data
    emp_id = pyip.inputInt(prompt="Masukkan nomor ID: ")

    for employee in data:
        if employee["ID"] == emp_id:
            print("Data karyawan dengan ID tersebut sudah ada.")
            continue_option = input("Apakah Anda ingin melanjutkan? (yes/no): ")
            if continue_option.lower() == "yes":
                create_employee()  # Recursively call create_employee to try adding a new employee
            return

    full_name = input("Masukkan nama lengkap: ")
    position = input("Masukkan jabatan: ")
    hiring_date = input("Masukkan tanggal kerja (YYYY-MM-DD): ")
    performance = input("Masukkan hasil performa: ")

    new_employee = {
        "nama_lengkap": full_name,
        "ID": emp_id,
        "jabatan": position,
        "tanggal_mulai_kerja": hiring_date,
        "performa": performance,
    }

    save_decision = input("Apakah Anda ingin menyimpan data baru? (yes/no): ")
    if save_decision.lower() == "yes":
        data.append(new_employee)
        print("Data karyawan berhasil disimpan.")
    else:
        print("Data karyawan tidak disimpan.")

    print("Data karyawan berhasil dibuat.")
    display_employee_data()
    
# Fungsi update karyawan
def update_employee():
    global data
    ID = pyip.inputInt(prompt="Masukkan ID karyawan yang ingin diupdate: ")

    for employee in data:
        if employee["ID"] == ID:
            print("Data karyawan:")
            print(tabulate([employee], headers="keys", tablefmt="pretty"))

            field_to_update = input("Bagian untuk diupdate (nama_lengkap/jabatan/tanggal_mulai_kerja/performa): ").strip()
            new_value = input(f"Masukkan nilai baru untuk {field_to_update}: ")

            if field_to_update in employee:
                employee[field_to_update] = new_value
                print("Data karyawan berhasil diupdate.")
                display_employee_data()
                return

    print("ID karyawan tidak ditemukan.")

# Fungsi menghapus karyawan
def delete_employee():
    global data
    emp_id = pyip.inputInt(prompt="Masukkan ID karyawan yang ingin dihapus: ")

    for employee in data:
        if employee["ID"] == emp_id:
            data.remove(employee)
            print("Data karyawan berhasil dihapus.")
            display_employee_data()
            return

    print("ID karyawan tidak ditemukan.")
    
# Categorize employees based on performance
def categorize_employees():
    categories = {
        "ajukan ke HRD": [],
        "naikkan performa": [],
        "rekomendasi untuk naikkan jabatan": []
    }

    for employee in data:
        if employee["performa"] == "sangat buruk":
            categories["ajukan ke HRD"].append(employee["nama_lengkap"])
        elif employee["performa"] in ["biasa", "bagus"]:
            categories["naikkan performa"].append(employee["nama_lengkap"])
        elif employee["performa"] == "sangat bagus":
            categories["rekomendasi untuk naikkan jabatan"].append(employee["nama_lengkap"])

    return categories

# Function to print categorized employee data
def print_categorized_data(categories):
    categorized_data = []

    for category, employees in categories.items():
        for employee in employees:
            categorized_data.append({'Kategori': category, 'Nama Karyawan': employee})

    print(tabulate(categorized_data, headers="keys", tablefmt="grid"))

# Main menu
def main_menu():
    while True:
        print("\nEmployee Data Management")
        print("1. Tunjukkan data karyawan")
        print("2. Buat data karyawan")
        print("3. Update data karyawan")
        print("4. Hapus karyawan")
        print("5. Klasifikasi performa karyawan")
        print("6. Exit")

        choice = input("Pilih opsi yang diinginkan: ")

        if choice == "1":
            display_employee_data()
        elif choice == "2":
            create_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "6":
            print("Selesai. Terima kasih!")
            break
        elif choice == "5":
            categories = categorize_employees()
            print_categorized_data(categories)
        else:
            print("Pilihan tidak ada. Harap diulang.")

if __name__ == "__main__":
    main_menu()
