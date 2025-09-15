# Leaderboard

A Python command-line program to calculate and display a ranking table for a league based on match results.

## Features

- Reads match results from standard input or a file.
- Supports all line endings (`\n`, `\r\n`, `\r`).
- Calculates points for each team (win: 3 pts, draw: 1 pt, loss: 0 pts).
- Outputs a sorted leaderboard.
- Handles invalid input gracefully.
- Includes automated tests.

## Prequisites

1. [Python3](https://www.python.org/downloads/)

## Usage

### Run the Program

You can run the program by piping input:

```bash
python ranking.py < sample.txt
```

Or by entering input manually (press Ctrl+D to end input):

```bash
python ranking.py
Team A 3, Team B 2
Team C 1, Team D 1
...
```

### Output

The program prints the leaderboard, sorted by points (and name for ties):

```
1. Team A, 3 pts
2. Team C, 1 pt
3. Team D, 1 pt
4. Team B, 0 pts
```

If no valid input is provided, it prints:

```
No valid input provided. Please see sample.txt for expected input format.
```

## Testing

Run the tests using:

```bash
python -m unittest test_ranking.py
```

## File Structure

- `ranking.py` - Main program logic.
- `test_ranking.py` - End to end Unit tests for the ranking logic using Python's subprocess library.
- `sample.txt` - Example input file.
- `Readme.md` - This documentation.

## Sample Input Format

Each line should be in the format:

```
Team Name 1 Score, Team Name 2 Score
```

Example:

```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```

## License

SABC TV license

---

**Created for coding test and leaderboard ranking demonstration.**