import subprocess
import unittest

class TestRanking(unittest.TestCase):
    def get_output(self, input_data):
        process = subprocess.run(
            ["python3", "ranking.py"],
            input=input_data,
            capture_output=True,
            text=True,
        )
        return process.stdout, process.stderr

    def test_ranking_with_sample_input(self):
        with open("sample.txt", "r") as f:
            input_data = f.read()

        output, error = self.get_output(input_data)

        expected_output = """1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
4. Snakes, 1 pt
5. Grouches, 0 pts
"""
        self.assertEqual(output, expected_output)
        self.assertEqual(error, "")

    def test_ranking_with_crlf_input(self):
        with open("sample-crlf.txt", "r") as f:
            input_data = f.read()

        output, error = self.get_output(input_data)

        expected_output = """1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
4. Snakes, 1 pt
5. Grouches, 0 pts
"""
        self.assertEqual(output, expected_output)
        self.assertEqual(error, "")

    def test_ranking_with_premierleague_input(self):
        with open("sample-premierleague.txt", "r") as f:
            input_data = f.read()

        output, error = self.get_output(input_data)

        expected_output = """1. Liverpool, 12 pts
2. Arsenal, 9 pts
3. Bournemouth, 9 pts
4. Tottenham Hotspur, 9 pts
5. Chelsea, 8 pts
6. Everton, 7 pts
7. Sunderland, 7 pts
8. Crystal Palace, 6 pts
9. Manchester City, 6 pts
10. Fulham, 5 pts
11. Newcastle United, 5 pts
12. Brentford, 4 pts
13. Brighton & Hove Albion, 4 pts
14. Leeds United, 4 pts
15. Manchester United, 4 pts
16. Nottingham Forest, 4 pts
17. Burnley, 3 pts
18. West Ham United, 3 pts
19. Aston Villa, 2 pts
20. Newcastle, 0 pts
21. Wolverhampton Wanderers, 0 pts
"""
        self.assertEqual(output, expected_output)
        self.assertEqual(error, "")

    def test_ranking_with_empty_input(self):
        with open("sample-empty.txt", "r") as f:
            input_data = f.read()

        output, error = self.get_output(input_data)

        expected_error = "No valid input provided. Please see sample.txt for expected input format.\n"
        self.assertEqual(output, "")
        self.assertEqual(error, expected_error)

    def test_ranking_with_invalid_input(self):
        with open("sample-invalid.txt", "r") as f:
            input_data = f.read()

        output, error = self.get_output(input_data)

        expected_error = """Skipping invalid line: I am a bird,
Skipping invalid line: I want...
Skipping invalid line: to
Skipping invalid line: fly!,,
No valid input provided. Please see sample.txt for expected input format.
"""
        self.assertEqual(output, "")
        self.assertEqual(error, expected_error)

if __name__ == "__main__":
    unittest.main()
