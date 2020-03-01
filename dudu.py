from time import sleep

ip_list=[]
ip_list.append(input("Enter first IP"))
ip_list.append(input("Enter 2nd IP"))
ip_list.append(input("Enter 3rd IP"))
ip_list.append(input("Enter 4th IP"))
ip_list.append(input("Enter 5th IP"))
print("\nThis is the list: " + str(ip_list))

new_ip=input("\nEnter new ip")
print("\nSearching...")
sleep(3)
if new_ip in ip_list:
    print("This IP is already exists")
else:
    print("Adding this IP...")
    sleep(3)
    ip_list.append(new_ip)

print("This is the new list: " + str(ip_list))


print("hasdsadaasdasdasdsdsadi")