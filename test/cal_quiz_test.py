import grader as g
import json
import os
import unittest

class CalQuizTest(unittest.TestCase):

    def test_quiz_01(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_01.png")

        with open("calQuiz/calQuiz_Page_01.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_01.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['D', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015596200')

    def test_quiz_02(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_02.png")

        with open("calQuiz/calQuiz_Page_02.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_02.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '016281261')

    def test_quiz_03(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_03.png")

        with open("calQuiz/calQuiz_Page_03.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_03.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '016005570')

    def test_quiz_04(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_04.png")

        with open("calQuiz/calQuiz_Page_04.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_04.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '015618079')

    def test_quiz_05(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_05.png")

        with open("calQuiz/calQuiz_Page_05.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_05.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015917963') 

    def test_quiz_06(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_06.png")

        with open("calQuiz/calQuiz_Page_06.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_06.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '015852729')

    def test_quiz_07(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_07.png")

        with open("calQuiz/calQuiz_Page_07.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_07.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '016117773')

    def test_quiz_08(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_08.png")

        with open("calQuiz/calQuiz_Page_08.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_08.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '015951334')

    def test_quiz_09(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_09.png")

        with open("calQuiz/calQuiz_Page_09.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_09.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['studentId'], '015949787')

    def test_quiz_10(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_10.png")

        with open("calQuiz/calQuiz_Page_10.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_10.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015764615')

    def test_quiz_11(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_11.png")

        with open("calQuiz/calQuiz_Page_11.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_11.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'A', '', '', '', ''])
        self.assertEqual(data['studentId'], '015685055')

    def test_quiz_12(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_12.png")

        with open("calQuiz/calQuiz_Page_12.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_12.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['', '', '', '', '', ''])
        self.assertEqual(data['studentId'], '016382687')

    def test_quiz_13(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_13.png")

        with open("calQuiz/calQuiz_Page_13.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_13.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '013776785')

    def test_quiz_14(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_14.png")

        with open("calQuiz/calQuiz_Page_14.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_14.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015374303')

    def test_quiz_15(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_15.png")

        with open("calQuiz/calQuiz_Page_15.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_15.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '014125861')

    def test_quiz_16(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_16.png")

        with open("calQuiz/calQuiz_Page_16.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_16.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015149936')

    def test_quiz_17(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_17.png")

        with open("calQuiz/calQuiz_Page_17.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_17.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['B', 'C', 'B', 'B', 'B', 'B'])
        self.assertEqual(data['studentId'], '010911247')

    def test_quiz_18(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_18.png")

        with open("calQuiz/calQuiz_Page_18.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_18.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015584149')

    def test_quiz_19(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_19.png")

        with open("calQuiz/calQuiz_Page_19.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_19.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '016187141')

    def test_quiz_20(self):
        grader = g.Grader()
        grader.grade("calQuiz/calQuiz_Page_20.png")

        with open("calQuiz/calQuiz_Page_20.png.json","r") as f:
            jsonData = f.read()
        os.remove("calQuiz/calQuiz_Page_20.png.json")

        data = json.loads(jsonData)

        self.assertEqual(data['answers'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['studentId'], '015664424')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalQuizTest)
    unittest.TextTestRunner(verbosity=2).run(suite)