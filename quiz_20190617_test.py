import unittest
import quiz_20190617

class TestFizz(unittest.TestCase):
    #FIXME -- if zero then 1 should be return as string because next increments
    def test_zero(self):
        buzzer = quiz_20190617.FizzBuzzer(0)
        self.assertEqual(buzzer.next(),'1')
    def test_one(self):
        buzzer = quiz_20190617.FizzBuzzer(1)
        self.assertEqual(buzzer.next(),'2')
    def test_two_four(self):
        #when `x = FizzBuzzer(2)`, `x.next()` returns `"fizz"` and calling `x.next()`
        #a second time returns `"4"`
        buzzer =quiz_20190617. FizzBuzzer(2)
        self.assertEqual(buzzer.next(),'fizz')     
        self.assertEqual(buzzer.next(),'4')   
   

if __name__=='__main__':

    unittest.main() 