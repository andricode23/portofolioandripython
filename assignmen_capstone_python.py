from tabulate import tabulate
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
    while True:
        print("\nTampilkan data karyawan")
        print("1. Tampilkan sebagian data karyawan")
        print("2. Tampilkan berdasarkan ID")
        print("3. Kembali ke menu utama")

        display_choice = pyip.inputChoice(["1", "2", "3"], prompt="Pilih opsi: ")

        if display_choice == "1":
            headers = ["nama_lengkap", "ID"]
            partial_data = [{key: employee[key] for key in headers} for employee in data]
            print(tabulate(partial_data, headers="keys", tablefmt="grid"))

            show_full_data = pyip.inputChoice(["yes", "no"], prompt="Apakah Anda ingin menampilkan seluruh data karyawan? (yes/no): ").lower()
            if show_full_data == "yes":
                print(tabulate(data, headers="keys", tablefmt="grid"))
        elif display_choice == "2":
            employee_id = pyip.inputInt(prompt="Masukkan ID karyawan yang ingin ditampilkan: ")
            display_employee_by_id(employee_id)
        elif display_choice == "3":
            break


 
def display_employee_by_id(employee_id):
    for employee in data:
        if employee["ID"] == employee_id:
            print(tabulate([employee], headers="keys", tablefmt="grid"))
            return
    print("ID karyawan nomor {} tidak ditemukan.".format(employee_id))       


def create_employee():
    global data
    while True:
        print("\nTambahkan Data Karyawan")
        print(tabulate(data, headers="keys", tablefmt="grid"))
        add_option = pyip.inputChoice(["1", "2"],  prompt="1. Kembali ke menu utama\n2. Lanjutkan menambahkan data karyawan\nPilih opsi: ")

        if add_option == "1":
            break  
        elif add_option == "2":
            emp_id = pyip.inputInt(prompt="Masukkan nomor ID: ")

            for employee in data:
                if employee["ID"] == emp_id:
                    print("Data karyawan dengan ID tersebut sudah ada.")
                    continue_option = pyip.inputChoice(["yes", "no"], prompt="Apakah Anda ingin memasukkan ID baru? (yes/no): ").lower()
                    if continue_option == "yes":
                        
                        continue
                    else:
                        
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

            
            confirm_add = pyip.inputChoice(["yes", "no"], prompt="Apakah Anda ingin menyimpan data baru? (yes/no): ").lower()
            if confirm_add == "yes":
                data.append(new_employee)
                print("Data karyawan berhasil disimpan.")
                print(tabulate(data, headers="keys", tablefmt="grid"))
            else:
                print("Data karyawan tidak disimpan.")
   
    
# Fungsi update karyawan
def update_employee():
    global data
    while True:
        print("\nUpdate Data Karyawan")
        print(tabulate(data, headers="keys", tablefmt="grid"))  
        update_option = pyip.inputChoice(["1", "2"],  prompt="1. Kembali ke menu utama\n2. Lanjutkan update data karyawan\nPilih opsi: ")

        if update_option == "1":
            break
        elif update_option == "2":
            emp_id = pyip.inputInt(prompt="Masukkan nomor ID: ")

            for employee in data:
                if employee["ID"] == emp_id:
                    while True:
                        print("Data karyawan:")
                        print(tabulate([employee], headers="keys", tablefmt="pretty"))

                        field_to_update = input("Bagian yang mau diupdate (nama_lengkap/jabatan/tanggal_mulai_kerja/performa): ").strip()

                        if field_to_update in employee:
                            current_value = employee[field_to_update]
                            new_value = input(f"Data saat ini: {current_value}\nMasukkan data baru untuk {field_to_update} (kosongkan jika tidak ingin mengubah): ").strip()

                            if new_value != "":
                                print(f"Data baru untuk {field_to_update}: {new_value}")
                                confirm_update = pyip.inputChoice(["yes", "no"], prompt="Apakah Anda yakin ingin menyimpan perubahan ini? (yes/no): ").lower()
                                if confirm_update == "yes":
                                    employee[field_to_update] = new_value
                                    print("Data karyawan berhasil diupdate.")
                                else:
                                    print("Perubahan dibatalkan.")
                            else:
                                print("Tidak ada perubahan pada data karyawan.")

                            print(tabulate(data, headers="keys", tablefmt="grid"))

                            continue_option = pyip.inputChoice(["yes", "no"], prompt="Apakah Anda ingin melanjutkan update? (yes/no): ").lower()
                            if continue_option == "no":
                                return  
                        else:
                            print("Bagian yang dimaksud tidak ada dalam data karyawan.")

                    break
            else:
                print("ID karyawan tidak ditemukan.")
        else:
            print("Pilihan tidak valid. Harap pilih 1 atau 2.")

# Fungsi menghapus karyawan
def delete_employee():
    global data
    while True:
        print("\nHapus Data Karyawan")
        print(tabulate(data, headers="keys", tablefmt="grid"))
        delete_option = pyip.inputChoice(["1", "2"], prompt="1. Kembali ke menu utama\n2. Lanjutkan menghapus data karyawan\nPilih opsi: ")

        if delete_option == "1":
            break  
        elif delete_option == "2":
            emp_id = pyip.inputInt(prompt="Masukkan ID karyawan yang ingin dihapus: ")

            for employee in data:
                if employee["ID"] == emp_id:
                    print("Data karyawan:")
                    print(tabulate([employee], headers="keys", tablefmt="pretty"))

                    confirm_delete = pyip.inputChoice(["yes", "no"], prompt="Apakah Anda yakin ingin menghapus data karyawan ini? (yes/no): ").lower()

                    if confirm_delete == "yes":
                        data.remove(employee)
                        print("Data karyawan berhasil dihapus.")
                        

                    continue_option = pyip.inputChoice(["1", "2"],  prompt="1. Kembali ke menu utama\n2. Lanjutkan menghapus data karyawan\nPilih opsi: ")

                    if continue_option == "1":
                        return  
                    elif continue_option == "2":
                        break  
                    else:
                        print("Pilihan tidak valid. Kembali ke menu utama.")
                    break
            else:
                print("ID karyawan tidak ditemukan.")
        else:
            print("Pilihan tidak valid. Harap pilih 1 atau 2.")


    
# klasifikasikan karyawan
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

# memasukkan dan membuat tabel klasifikasi karyawan.
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

