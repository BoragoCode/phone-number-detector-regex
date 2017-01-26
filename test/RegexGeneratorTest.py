import unittest

from application.RegexGenerator import RegexGenerator


class TestRegexGenerator(unittest.TestCase):

    regex_generator = None;

    def setUp(self):
        self.regex_generator = RegexGenerator()

    def test_number_dictionary_exist(self):
        self.assertIsNotNone(self.regex_generator.NUMBER_DICTIONARY)

    def test_given_phones_list_of_one(self):
        phones = [635]
        expected_output = "(6|seis)(.|\n|\t)*(3|tres)(.|\n|\t)*(5|cinco)"
        self.assertEqual(self.regex_generator.build_phones_regex(phones), expected_output)

    def test_given_phones_list_must_create_regex(self):
        phones = [982, 645]
        expected_output = "(((9|nueve)(.|\n|\t)*(8|ocho)(.|\n|\t)*(2|dos))|((6|seis)(.|\n|\t)*(4|cuatro)(.|\n|\t)*(5|cinco)))"
        self.assertEqual(self.regex_generator.build_phones_regex(phones), expected_output)


    def test_given_phones_list_must_create_regex(self):
        phones = [640571510, 345876234]
        expected_output = "(((6|seis)(.|\n|\t)*(4|cuatro)(.|\n|\t)*(0|cero)(.|\n|\t)*(5|cinco)(.|\n|\t)*(7|siete)(.|\n|\t)*(1|uno)(.|\n|\t)*(5|cinco)(.|\n|\t)*(1|uno)(.|\n|\t)*(0|cero))|((3|tres)(.|\n|\t)*(4|cuatro)(.|\n|\t)*(5|cinco)(.|\n|\t)*(8|ocho)(.|\n|\t)*(7|siete)(.|\n|\t)*(6|seis)(.|\n|\t)*(2|dos)(.|\n|\t)*(3|tres)(.|\n|\t)*(4|cuatro)))"
        self.assertEqual(self.regex_generator.build_phones_regex(phones), expected_output)
