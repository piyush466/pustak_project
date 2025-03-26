# # list = [2,3,4,61,23,4,6,3,4,5,6,4,3]
# #
# # print(sorted(list))
# import configparser
#
# config = configparser.ConfigParser()
# config.read(r"config\\config.ini")
#
# print(config["URL"]["URL"])
# # print(config.sections())
# from pythonProject.utilities.logger import setup_logger
#
# # Fetch URL if section exists
#
# log = setup_logger()
# log.info("testtsdagg")

# import datetime
#
# now = datetime.datetime.now()
#
# # Extract time without milliseconds
# current_time = now.strftime("%H:%M:%S")
# print(current_time)


# import os
# from dotenv import load_dotenv
#
# # Provide the correct .env file path
# env_path = r"C:\Users\Piyush Dravyakar\Pustak_project\pythonProject\.env"
#
# # Load environment variables from the .env file
# load_dotenv(env_path)
#
# # Get environment variable
# username = os.getenv("USEREMAIL")  # Ensure it matches the key in the .env file
#
# # Print the value
# print(f"Username: {username}")

# a = 3,4,5
#
# a.count()
# print(a)

string = "piyush"
new_string = ""

# print(string[::-1])

# for i in range(len(string)-1,-1,-1):
#     print(string[i],end="")





# for i in range(len(string)-1,-1,-1):
#     print(i,string[i])
#     new_string = new_string + string[i]
#
# print(new_string)

# print(string[::-1])


# list = [4,1,5,9,2,6]

# def largest_second_number(list):
#     new_sorted = sorted(list)
#     # print(new_sorted)
#     return (new_sorted[::-1][1])
#
# new_largest = largest_second_number([4,1,5,9,2,6])
# print(new_largest)


# lista = [12,23,4,112,3,23]
#
# newL = []
# lista.reverse()
# print(lista)
# print(list(reversed(lista)))

my_list = [12, 23, 4, 112, 3, 23]

my_list.reverse()  # Reverses the list in place
print(my_list)







# for i in range(len(list)-1,-1,-1):
#     print(i,list[i])
#     newL.append(list[i])
#
# print(newL)
