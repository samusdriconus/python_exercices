import unittest
import lottery_game

def check_range(container,low,high):
    for el in container:
        if el < low or el > high:
            return False
    return True


class TestLottery(unittest.TestCase):
    def test_count(self):
        output = lottery_game.generate_output()
        count = len(output)
        self.assertEqual(count,10) 
    def test_range(self):
        output = lottery_game.generate_output()
        condition = check_range(output,1,50)
        self.assertEqual(condition,True)
    def test_sorting(self):
        output = lottery_game.generate_output()
        output_sorted = output[:]
        output_sorted.sort()
        self.assertEqual(output,output_sorted)
    

    

if __name__ == '__main__':
    unittest.main()