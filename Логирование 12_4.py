import unittest
import rt_with_exceptions
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r_w_t = rt_with_exceptions
            runner_1 = r_w_t.Runner('Mikhail', -30)
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 30)
            logging.info(f'"test_walk" пройден успешно {runner_1}')
        except ValueError:
            logging.warning('Скорость для Runner не верна', exc_info=True)

    def test_run(self):
        try:
            r_w_t = rt_with_exceptions
            runner_1 = r_w_t.Runner(200, 50)
            for i in range(10):
                runner_1.run()
            self.assertEqual(runner_1.distance, 100)
            logging.info('"test_run" пройден успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return 0

    def test_challenge(self):
        r_w_t = rt_with_exceptions
        runner_2 = r_w_t.Runner('Hasan')
        runner_3 = r_w_t.Runner('Svyt')
        for i in range(10):
            runner_2.walk()
            runner_3.run()
        self.assertNotEqual(runner_2.distance, runner_3.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

if __name__ == '__main__':
    unittest.main()