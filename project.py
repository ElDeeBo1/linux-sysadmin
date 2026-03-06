import subprocess

def Run_Command(cmd):
   try:
         result=subprocess.run(cmd,shell=True,capture_output=True,text=True)

   except subprocess.CalledProcessError as e:
        print(f"Error:{e}")

# def Add_User():
#      username= input("Enter username: ")
#      password= input("Enter password: ")
#      Run_Command(f"sudo useradd {username}")
#      Run_Command(f"echo '{username}:{password}' | sudo chpasswd ")
#      print(f"user {username} added successfully")
# Add_User()

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

Modify_User()

# def Delete_User():
#      username=input("Enter username: ")
#      Run_Command(f"sudo userdel -r {username}")
#      print(f"user {username} deleted successfully")
# Delete_User()   

