import custom_grader as g
import json
import os
import unittest


class CalQuizTest(unittest.TestCase):

    def test_quiz_1_01(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_01.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['D', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '5', '9', '6', '2', '0', '0'])

    def test_quiz_1_02(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_02.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '2', '8', '1', '2', '6', '1'])

    def test_quiz_1_03(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_03.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '0', '0', '5', '5', '7', '0'])

    def test_quiz_1_04(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_04.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '6', '1', '8', '0', '7', '9'])

    def test_quiz_1_05(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_05.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '9', '1', '7', '9', '6', '3']) 

    def test_quiz_1_06(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_06.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '8', '5', '2', '7', '2', '9'])

    def test_quiz_1_07(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_07.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '1', '1', '7', '7', '7', '3'])

    def test_quiz_1_08(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_08.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '9', '5', '1', '3', '3', '4'])

    def test_quiz_1_09(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_09.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '9', '4', '9', '7', '8', '7'])

    def test_quiz_1_10(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_10.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '7', '6', '4', '6', '1', '5'])

    def test_quiz_1_11(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_11.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'A', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '6', '8', '5', '0', '5', '5'])

    def test_quiz_1_12(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_12.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '3', '8', '2', '6', '8', '7'])

    def test_quiz_1_13(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_13.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '3', '7', '7', '6', '7', '8', '5'])

    def test_quiz_1_14(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_14.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '3', '7', '4', '3', '0', '3'])

    def test_quiz_1_15(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_15.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '1', '2', '5', '8', '6', '1'])

    def test_quiz_1_16(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_16.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '1', '4', '9', '9', '3', '6'])

    def test_quiz_1_17(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_17.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'C', 'B', 'B', 'B', 'B'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '0', '9', '1', '1', '2', '4', '7'])

    def test_quiz_1_18(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_18.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '5', '8', '4', '1', '4', '9'])

    def test_quiz_1_19(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_19.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '1', '8', '7', '1', '4', '1'])

    def test_quiz_1_20(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_1/calQuiz_Page_20.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '6', '6', '4', '4', '2', '4'])
    
    def test_quiz_2_01(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_01.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '0', '4', '2', '0', '3', '5'])

    def test_quiz_2_02(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_02.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', '-', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '5', '2', '8', '1', '3', '3'])

    def test_quiz_2_03(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_03.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['?', 'A', '?', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '3', '6', '0', '2', '2', '4'])

    def test_quiz_2_04(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_04.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '3', '1', '5', '3', '3', '4'])

    def test_quiz_2_05(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_05.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '0', '4', '0', '2', '9', '3'])

    def test_quiz_2_06(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_06.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '5', '9', '9', '3', '7', '2'])

    def test_quiz_2_07(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_07.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'C', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '3', '8', '4', '4', '0', '4'])

    def test_quiz_2_08(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_08.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '7', '8', '5', '4', '2', '8'])

    def test_quiz_2_09(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_09.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['E', 'E', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '2', '1', '1', '0', '8', '7'])

    def test_quiz_2_10(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_10.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'E', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '2', '5', '3', '3', '9', '5', '9'])

    def test_quiz_2_11(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_11.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '9', '8', '8', '5', '5', '3'])

    def test_quiz_2_12(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_12.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', '-', 'A', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '0', '5', '5', '8', '1', '5'])

    def test_quiz_2_13(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_13.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '7', '3', '8', '9', '4', '0'])

    def test_quiz_2_14(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_14.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '9', '6', '4', '2', '4', '3'])

    def test_quiz_2_15(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_15.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'C', 'C', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '1', '4', '6', '7', '5', '0'])

    def test_quiz_2_16(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_16.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['1', '0', '5', '8', '0', '9', '8', '6', '8'])

    def test_quiz_2_17(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_17.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '3', '5', '9', '9', '7', '7'])

    def test_quiz_2_18(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_18.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['?', 'E', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '3', '0', '2', '3', '4', '7'])

    def test_quiz_2_19(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_19.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '7', '3', '6', '4', '3', '1'])

    def test_quiz_2_20(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_20.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'C', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '2', '9', '4', '3', '2', '7'])

    def test_quiz_2_21(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_21.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '9', '1', '5', '7', '1', '4'])

    def test_quiz_2_22(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_22.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '1', '6', '2', '5', '4', '5'])

    def test_quiz_2_23(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_23.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'C', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '0', '7', '3', '1', '9', '6'])

    def test_quiz_2_24(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_24.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '1', '5', '1', '6', '9', '1'])

    def test_quiz_2_25(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_25.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'C', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '1', '7', '2', '8', '6', '7'])

    def test_quiz_2_26(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_26.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '2', '2', '3', '8', '0', '2'])

    def test_quiz_2_27(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_27.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '3', '0', '4', '2', '7', '2'])

    def test_quiz_2_28(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_2/quiz2_Page_28.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'A', 'B', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '3', '3', '6', '5', '2', '4'])

    def test_quiz_3_05(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-05.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '0', '1', '8', '9', '7', '3']) 

    def test_quiz_3_06(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-06.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '2', '4', '8', '8', '0', '6', '9'])

    def test_quiz_3_07(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-07.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '4', '1', '1', '7', '9', '6'])

    def test_quiz_3_08(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-08.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['D', 'A', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '5', '8', '9', '0', '5', '1'])

    def test_quiz_3_09(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-09.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '4', '1', '3', '3', '0', '2'])

    def test_quiz_3_10(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-10.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '2', '8', '6', '2', '6', '8'])

    def test_quiz_3_11(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-11.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'])

    def test_quiz_3_12(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-12.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '0', '0', '5', '3', '4', '9'])

    def test_quiz_3_13(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-13.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '7', '4', '6', '8', '7', '0'])

    def test_quiz_3_14(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-14.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '8', '3', '8', '3', '6', '4'])

    def test_quiz_3_15(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-15.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '6', '0', '6', '3', '4', '0'])

    def test_quiz_3_16(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-16.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '8', '7', '0', '1', '2', '3'])

    def test_quiz_3_17(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-17.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '2', '6', '8', '7', '5', '5'])

    def test_quiz_3_18(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-18.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '0', '5', '7', '4', '6', '6'])

    def test_quiz_3_19(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-19.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '5', '6', '3', '8', '8', '2'])

    def test_quiz_3_20(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-20.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '5', '8', '8', '5', '1', '7'])

    def test_quiz_3_21(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-21.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'])

    def test_quiz_3_22(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-22.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['E', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '9', '2', '9', '9', '3', '6'])

    def test_quiz_3_23(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-23.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'])

    def test_quiz_3_24(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-24.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '3', '7', '3', '3', '3', '0', '0'])

    def test_quiz_3_25(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-25.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '1', '5', '6', '4', '8', '7'])

    def test_quiz_3_26(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-26.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '0', '5', '6', '6', '4', '9', '4', '4'])

    def test_quiz_3_27(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-27.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '3', '4', '3', '6', '7', '6'])

    def test_quiz_3_28(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-28.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['E', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '6', '5', '5', '8', '7', '0'])

    def test_quiz_3_29(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-29.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '7', '6', '7', '0', '0', '7'])

    def test_quiz_3_30(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-30.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '3', '5', '9', '4', '5', '7'])

    def test_quiz_3_31(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-31.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['D', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '6', '2', '7', '3', '7', '4', '7'])

    def test_quiz_3_32(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-32.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '6', '6', '3', '7', '7', '5'])

    def test_quiz_3_33(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-33.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '5', '8', '5', '7', '1', '0'])

    def test_quiz_3_34(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-34.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '6', '9', '6', '1', '4', '5'])

    def test_quiz_3_35(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-35.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '0', '6', '6', '1', '7', '8'])

    def test_quiz_3_36(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-36.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '3', '9', '7', '5', '7', '8', '9'])

    def test_quiz_3_37(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-37.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '4', '1', '3', '9', '7', '9', '7'])

    def test_quiz_3_38(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-38.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '6', '2', '6', '8', '2', '8'])

    def test_quiz_3_39(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-39.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['-', '-', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '9', '7', '3', '2', '6', '5'])

    def test_quiz_3_40(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-40.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['B', 'C', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '5', '2', '2', '2', '5', '2', '8'])

    def test_quiz_3_41(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-41.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['A', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['0', '1', '3', '4', '5', '8', '3', '1', '1'])

    def test_quiz_3_42(self):
        grader = g.CustomGrader()
        jsonData = grader.grade('images/6q/set_3/image-42.png', False, False)
        data = json.loads(jsonData)

        self.assertEqual(data['answer']['bubbled'], ['C', 'B', '-', '-', '-', '-'])
        self.assertEqual(data['version']['bubbled'], ['-'])
        self.assertEqual(data['id']['bubbled'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalQuizTest)
    unittest.TextTestRunner(verbosity=2).run(suite)