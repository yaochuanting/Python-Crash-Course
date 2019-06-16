# # 编写一个使用name_function的程序。程序names.py让用户输入名和姓，并显示整洁的全名：
# from name_function import get_formatted_name
#
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give a last name: ")
#     if last == 'q':
#         break
#
#     formatted_name = get_formatted_name(first, last)
#     print("\tNeatly formatted name: " + formatted_name + ".")






# 检查函数get_formatted_name()在给定名和姓时 能否正确地工作
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()


