#Jennifer Jenkins June 17
import unittest

class FizzBuzzer:
    def __init__(self, start=0):
        self.number=start
    
    def next(self):
        self.number+=1
        
        if self.number%3==0 and self.number%5==0:
            return "fizzbuzz"
        if self.number%3==0:
            return "fizz"
        elif self.number%5==0:
            return "buzz"
        else:
            return str(self.number)

    
        #FIXME --normal, not class method.  Confirm what that means -- defined completely outside of class?
    
#watch out for what the value is before and after next runs!

class TestFizz(unittest.TestCase):
    #FIXME -- if zero then 1 should be return as string because next increments
    def test_zero(self):
        buzzer = FizzBuzzer(0)
        self.assertEquals(buzzer.next(),'1')
    def test_one(self):
        buzzer = FizzBuzzer(1)
        self.assertEquals(buzzer.next(),'2')
    def test_two_four(self):
        #when `x = FizzBuzzer(2)`, `x.next()` returns `"fizz"` and calling `x.next()`
        #a second time returns `"4"`
        buzzer = FizzBuzzer(2)
        self.assertEquals(buzzer.next(),'fizz')     
        self.assertEquals(buzzer.next(),'4')   
   

if __name__=='__main__':

    unittest.main() 


    buzzer = FizzBuzzer(0)
    print(buzzer.next())
    print(buzzer.next())
    print(buzzer.next())
    print(buzzer.next())
    print(buzzer.next())
    
    




    
    