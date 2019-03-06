import grader as g
import json
import os
import unittest


class CalQuizTest(unittest.TestCase):

    def test_quiz_01(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_01.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['D', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015596200')

    def test_quiz_02(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_02.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016281261')

    def test_quiz_03(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_03.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016005570')

    def test_quiz_04(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_04.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015618079')

    def test_quiz_05(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_05.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015917963') 

    def test_quiz_06(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_06.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015852729')

    def test_quiz_07(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_07.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016117773')

    def test_quiz_08(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_08.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015951334')

    def test_quiz_09(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_09.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015949787')

    def test_quiz_10(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_10.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015764615')

    def test_quiz_11(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_11.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'A', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015685055')

    def test_quiz_12(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_12.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016382687')

    def test_quiz_13(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_13.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '013776785')

    def test_quiz_14(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_14.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015374303')

    def test_quiz_15(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_15.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014125861')

    def test_quiz_16(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_16.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015149936')

    def test_quiz_17(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_17.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'C', 'B', 'B', 'B', 'B'])
        self.assertEqual(data['id']['bubbled'], '010911247')

    def test_quiz_18(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_18.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015584149')

    def test_quiz_19(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_19.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016187141')

    def test_quiz_20(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/calQuiz_Page_20.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015664424')

    def test_quiz_2_01(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_01.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016042035')

    def test_quiz_2_02(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_02.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', '', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014528133')

    def test_quiz_2_03(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_03.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015360224')

    def test_quiz_2_04(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_04.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016315334')

    def test_quiz_2_05(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_05.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016040293')

    def test_quiz_2_06(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_06.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015599372')

    def test_quiz_2_07(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_07.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'C', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015384404')

    def test_quiz_2_08(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_08.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015785428')

    def test_quiz_2_09(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_09.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['E', 'E', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016211087')

    def test_quiz_2_10(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_10.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'E', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '012533959')

    def test_quiz_2_11(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_11.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015988553')

    def test_quiz_2_12(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_12.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', '', 'A', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016055815')

    def test_quiz_2_13(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_13.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015738940')

    def test_quiz_2_14(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_14.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015964243')

    def test_quiz_2_15(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_15.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'C', 'C', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016146750')

    def test_quiz_2_16(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_16.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '105809868')

    def test_quiz_2_17(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_17.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015359977')

    def test_quiz_2_18(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_18.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'E', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016302347')

    def test_quiz_2_19(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_19.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015736431')

    def test_quiz_2_20(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_20.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'C', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015294327')

    def test_quiz_2_21(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_21.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015915714')

    def test_quiz_2_22(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_22.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016162545')

    def test_quiz_2_23(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_23.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'C', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016073196')

    def test_quiz_2_24(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_24.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015151691')

    def test_quiz_2_25(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_25.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'C', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016172867')

    def test_quiz_2_26(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_26.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015223802')

    def test_quiz_2_27(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_27.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015304272')

    def test_quiz_2_28(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz2/quiz2_Page_28.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'A', 'B', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016336524')

    def test_quiz_3_05(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-05.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016018973') 
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_06(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-06.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '012488069')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_07(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-07.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014411796')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_08(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-08.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['D', 'A', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014589051')
        self.assertEqual(data['version']['bubbled'], '') 

    def test_quiz_3_09(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-09.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016413302')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_10(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-10.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014286268')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_11(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-11.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '---------')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_12(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-12.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016005349')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_13(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-13.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015746870')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_14(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-14.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015838364')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_15(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-15.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015606340')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_16(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-16.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015870123')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_17(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-17.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016268755')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_18(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-18.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016057466')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_19(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-19.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015563882')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_20(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-20.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015588517')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_21(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-21.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '---------')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_22(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-22.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['E', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015929936')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_23(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-23.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '---------')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_24(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-24.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '013733300')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_25(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-25.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016156487')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_26(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-26.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '005664944')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_27(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-27.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014343676')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_28(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-28.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['E', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015655870')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_29(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-29.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015767007')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_30(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-30.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015359457')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_31(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-31.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['D', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '016273747')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_32(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-32.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014663775')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_33(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-33.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014585710')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_34(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-34.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014696145')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_35(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-35.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014066178')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_36(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-36.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '013975789')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_37(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-37.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014139797')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_38(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-38.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015626828')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_39(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-39.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015973265')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_40(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-40.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['B', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015222528')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_41(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-41.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '013458311')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_3_42(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz3/image-42.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '---------')
        self.assertEqual(data['version']['bubbled'], '')

    def test_quiz_4_01(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz4/image-01.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['A', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014029856')

    def test_quiz_4_02(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz4/image-02.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['', '', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014504694')

    def test_quiz_4_03(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz4/image-03.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'C', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '014518565')

    def test_quiz_4_04(self):
        grader = g.Grader()
        jsonData = grader.grade("calQuiz/quiz4/image-04.png", True)
        data = json.loads(jsonData)

        self.assertEqual(data['answers']['bubbled'], ['C', 'B', '', '', '', ''])
        self.assertEqual(data['id']['bubbled'], '015297655')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalQuizTest)
    unittest.TextTestRunner(verbosity=2).run(suite)