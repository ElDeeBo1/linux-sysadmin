import subprocess

def Run_Command(cmd):
   try:
         result=subprocess.run(cmd,shell=True,capture_output=True,text=True)
         if result.stdout:
            print(result.stdout.strip())  # .strip() لإزالة السطور الفارغة في البداية أو النهاية
         if result.stderr:
            print("Error:", result.stderr.strip())
   except subprocess.CalledProcessError as e:
        print(f"Error:{e}")

def Add_User():
     username= input("Enter username: ")
     password= input("Enter password: ")
     Run_Command(f"sudo useradd {username}")
     Run_Command(f"echo '{username}:{password}' | sudo chpasswd ")
     print(f"user {username} added successfully")

def Modify_User():
    print("Modify User Options:")
    print("1. Change username")
    print("2. Change primary group")
    print("3. Add to supplementary group")
    print("4. Remove from supplementary group")
    choice = input("Select an option: ")

    username = input("Enter the existing username: ")
    if choice =="1" :
        new_name = input("Enter new username: ")
        Run_Command(f"sudo usermod -l {username}")
        print(f"Username changed from '{username}' to '{new_name}'")
    elif choice =="2":
        new_group = input("Enter new primary group: ")
        Run_Command(f"sudo usermod -g {new_group} {username}" )
        print(f"Primary group of '{username}' changed to '{new_group}'")
    elif choice =="3":
        new_group = input("Enter new secondary group: ")
        Run_Command(f"sudo usermod -aG {new_group} {username}" )
        print(f"Primary group of '{username}' changed to '{new_group}'")
    elif choice=="4":
        group = input("Enter group to remove: ")
        Run_Command(f"sudo gpasswd -d {username} {group}")
        print(f"User '{username}' removed from group '{group}'")
    else:
        print(" Invalid option")

def Delete_User():
     username=input("Enter username: ")
     Run_Command(f"sudo userdel -r {username}")
     print(f"user {username} deleted successfully")

def List_Users():
    Run_Command("cut -d: -f1 /etc/passwd") 

def add_group():
    groupname = input("Enter new group name: ")
    Run_Command(f"sudo groupadd {groupname}")
    print(f"Group '{groupname}' added successfully!")

def delete_group():
    groupname = input("Enter group name to delete: ")
    Run_Command(f"sudo groupdel {groupname}")
    print(f" Group '{groupname}' deleted successfully!")

def lock_user():
    username = input("Enter username to lock: ")
    change_password(f"sudo passwd -l {username}")
    print(f"User '{username}' locked!")


def unlock_user():
    username = input("Enter username to unlock: ")
    Run_Command(f"sudo passwd -u {username}")
    print(f"User '{username}' unlocked!")

def change_password():
    username = input("Enter username to change password: ")
    password = input("Enter new password: ")
    Run_Command(f"echo '{username}:{password}' | sudo chpasswd")
    print(f" Password for '{username}' changed!")


def main_menu():
    while True:
        print("\n=== Linux User Management Menu ===")
        print("1. Add User")
        print("2. Modify User")
        print("3. Delete User")
        print("4. List Users")
        print("5. Add Group")
        print("6. Delete Group")
        print("7. Lock User")
        print("8. Unlock User")
        print("9. Change Password")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            Add_User()
        elif choice == "2":
            Modify_User()
        elif choice == "3":
            Delete_User()
        elif choice == "4":
            List_Users()
        elif choice == "5":
            add_group()
        elif choice == "6":
            delete_group()
        elif choice == "7":
            lock_user()
        elif choice == "8":
            unlock_user()
        elif choice == "9":
            change_password()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main_menu()