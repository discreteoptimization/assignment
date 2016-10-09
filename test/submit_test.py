import sys, os, pytest

sys.path.append('.')
import submit

output_worked = 'Your submission has been accepted and will be graded shortly.'

from io import StringIO 

class TestCorrectMetadata:
    def test_001(self):
        meta_data = submit.load_metadata('test/_coursera')
        assert len(meta_data.part_data) == 6

class TestBrokenMetadata:
    # file not found
    def test_001(self):
        with pytest.raises(SystemExit):
            submit.load_metadata('test/_missing')

    # bad meta data format
    def test_002(self):
        with pytest.raises(SystemExit):
            submit.load_metadata('test/_empty')


class TestLogin:
    def setup_class(self):
        self.parser = submit.build_parser()

    def test_001(self):
        sys.stdin = StringIO(u'username\ntoken\n')
        login, token = submit.login_prompt('')
        assert(login == 'username')
        assert(token == 'token')

    def test_002(self):
        login, token = submit.login_prompt('test/_credentials')
        assert(login == 'cj@coffr.in')
        assert(token == '0GHf4Kfxa2CFWJoK')

    # testing manual override when credentials file is incorrect
    # def test_003(self, capfd):
    #     login, token = submit.login_prompt('test/_credentials')
    #     sys.stdin = StringIO(u'1\n%s\n%s\n' % (login, token))
        
    #     submit.main(self.parser.parse_args(['-o', './test/model/model.mzn', '-m', './test/_coursera', '-c', './test/_credentials3']))

    #     resout, reserr = capfd.readouterr()
    #     assert(output_worked in resout)


class TestPartsPrompt:
    def setup_class(self):
        self.metadata = submit.load_metadata('test/_coursera')

    def test_001(self, capfd):
        sys.stdin = StringIO(u'0.1\n1\n')
        problems = submit.part_prompt(self.metadata.part_data)
        assert(len(problems) == 1)

        resout, reserr = capfd.readouterr()
        assert('It is not an integer.' in resout)

    def test_002(self, capfd):
        sys.stdin = StringIO(u'100\n1\n')
        problems = submit.part_prompt(self.metadata.part_data)
        assert(len(problems) == 1)

        resout, reserr = capfd.readouterr()
        assert('It is out of the valid range' in resout)

    def test_003(self, capfd):
        sys.stdin = StringIO(u'-1\n1\n')
        problems = submit.part_prompt(self.metadata.part_data)
        assert(len(problems) == 1)

        resout, reserr = capfd.readouterr()
        assert('It is out of the valid range' in resout)

    def test_004(self, capfd):
        sys.stdin = StringIO(u'1,2\n')
        problems = submit.part_prompt(self.metadata.part_data)
        assert(len(problems) == 2)

    def test_005(self, capfd):
        sys.stdin = StringIO(u'0\n')
        problems = submit.part_prompt(self.metadata.part_data)
        assert(len(problems) == len(self.metadata.part_data))


class TestProblemSubmission:
    def setup_class(self):
        self.parser = submit.build_parser()

    # # tests problem selection
    # def test_001(self, capfd):
    #     sys.stdin = StringIO(u'1\n')
    #     submit.main(self.parser.parse_args(['-m', './test/_coursera', '-c', './test/_credentials']))

    #     output = 'Unable to locate assignment file'
    #     resout, reserr = capfd.readouterr()
    #     assert(output in resout)

    # tests running a problem
    def test_002(self, capfd):
        sys.stdin = StringIO(u'1\n')
        submit.main(self.parser.parse_args(['-m', './test/_coursera', '-c', './test/_credentials']))

        resout, reserr = capfd.readouterr()
        assert(output_worked in resout)

    # tests running a problem in record mode
    def test_003(self, capfd):
        sys.stdin = StringIO(u'1\n')
        submit.main(self.parser.parse_args(['-m', './test/_coursera', '-c', './test/_credentials', '-rs']))

        output = 'writting submission file: _awPVV'
        resout, reserr = capfd.readouterr()
        assert(output in resout)
        assert(not output_worked in resout)

        os.remove('_awPVV/submission.sub')
        os.rmdir('_awPVV')

    # tests running a solver with a int return value
    def test_004(self, capfd):
        sys.stdin = StringIO(u'2\n')
        submit.main(self.parser.parse_args(['-m', './test/_coursera', '-c', './test/_credentials']))

        resout, reserr = capfd.readouterr()
        assert(output_worked in resout)

    # tests running a solver with a unicode return value
    def test_005(self, capfd):
        sys.stdin = StringIO(u'3\n')
        submit.main(self.parser.parse_args(['-m', './test/_coursera', '-c', './test/_credentials']))

        resout, reserr = capfd.readouterr()
        assert(output_worked in resout)



# class TestBrokenSubmission:
#     def setup_method(self, _):
#         self.parser = submit.build_parser()

#     # should throw incorrect problem parts
#     def test_001(self, capfd):
#         sys.stdin = StringIO(u'1\n')
#         submit.main(self.parser.parse_args(['-m', './test/_coursera3', '-c', './test/_credentials2', '-o', './test/model/model.mzn']))

#         output_1 = 'Unexpected response code, please contact the course staff.'
#         output_2 = 'Expected parts: '
#         output_3 = 'but found: '
#         resout, reserr = capfd.readouterr()
#         print(resout)
#         assert(output_1 in resout)
#         assert(output_2 in resout)
#         assert(output_3 in resout)

#     # should throw incorrect login details
#     def test_002(self, capfd):
#         sys.stdin = StringIO(u'1\n')
#         submit.main(self.parser.parse_args(['-m', './test/_coursera3', '-c', './test/_credentials', '-o', './test/model/model.mzn']))
        
#         output = 'Please use a token for the assignment you are submitting.'
#         resout, reserr = capfd.readouterr()
#         print(resout)
#         assert(output in resout)


