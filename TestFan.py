#Import the fan program file
from Fan import*

#Create a class to test the program
class TestFan:
#Create 2 test variables with the given properties
    def main():
        fan1 = Fan(Fan.FAST, 10.00, 'yellow', True)
        fan2 = Fan(Fan.MEDIUM, 5.00, 'blue', False)
#Print the properties given
        print("TestFan 1:")
        print("Fan Speed:", fan1.get_fanspeed())
        print("Fan Radius:", fan1.get_fanradius())
        print("Fan Color:", fan1.get_fancolor())
        print("Turned On?:", fan1.get_fanon())

        print("\nTestFan 2:")
        print("Fan Speed:", fan2.get_fanspeed())
        print("Fan Radius:", fan2.get_fanradius())
        print("Fan Color:", fan2.get_fancolor())
        print("Turned On?:", fan2.get_fanon())
#Start the test program
    if __name__ == '__main__':
        main()
