import unittest 

class UCTestCase(unittest.TestCase):
    def setUp(self):
        #测试前需执行的操作
        print('setUP')  
    def tearDown(self):
        #测试用例执行完后所需执行的操作
        print('tearDown')      
    # 测试用例1
    def testCreateFolder(self):
        #具体的测试脚本
        print(1)
    # 测试用例2
    def testDeleteFolder(self):
        #具体的测试脚本
        print(2)
        self.assertFalse(True)
    def testEndFolder(self):
        #具体的测试脚本
        print(3)
if __name__ == "__main__":
    unittest.main()
