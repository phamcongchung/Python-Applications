#input: number of ppl in phonebook(>0,<6), repeat input name, phone number of each
#output: random name, if exist, print out; else print not exist
import sys
def main():
    n = int(input("Number of people: "))
    while n<0 or n>6:
        n = int(input("Retpye: "))
    phonebook = {}
    for i in range(n):
        phonebook.update({input("Name: "):input("Phone number: ")})
    name = input("Search: ")
    if name in phonebook:
        print(phonebook[name])
        sys.exit(0)
    print("Not exist")
    sys.exit(1)
if __name__ == "__main__":
    main() 