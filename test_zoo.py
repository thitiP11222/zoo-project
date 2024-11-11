import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
        
    # Child test 0-12
    def test1_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    def test2_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
        
    # Teen test 13-20
    def test1_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)  
    def test2_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)  
        
    # Adult test 21-60
    def test1_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)  
    def test2_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)  
        
    # Elderly test >60
    def test1_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)  
    def test2_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)     
          
    # Invalid age test
    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "invalid age")  
if __name__ == '__main__':
    unittest.main()