def main():
    while True:
     number = int(input("Give a number"))
     
     if (number <0):
       print("Unsuitable number")
       continue

     if (number == 0):
      break

     if (number >0):
       print(number * number)
       continue
       
if __name__ == '__main__':
    main()
