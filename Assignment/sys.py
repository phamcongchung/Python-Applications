import sys
def main():
    list_name = ["Tuan","Minh","Hung"]
    if "Tuan" in list_name:
        print("Exist")
        sys.exit(0)
    print ("Not exist")
    sys.exit(1)

if __name__ == "__main__":
    main()