from screenshotter import Screenshotter
from debug_wrapper import DebugWrapper
import csv
import os

class Runner:
    def __init__(self):
        self.screenshotter = Screenshotter()
        self.screenshotter = DebugWrapper(self.screenshotter)

    def login(self):
        self.screenshotter.login()
    
    def solve_problem(self, link, fileName):
        self.screenshotter.load_page(link)
        height = self.screenshotter.get_height()
        self.screenshotter.screenshot_problem(height, fileName)

if __name__ == "__main__":
    runner = Runner()
    runner.login()

    # loop through each problem, and solve
    with open('data/problem_data.csv', 'r') as file:
        csv_reader = csv.reader(file)

        # Convert the CSV reader object to a list of rows
        rows = list(csv_reader)

        # Access specific rows by index
        for row in rows[1:]:
            number = row[0]
            problem_title = row[1]
            link = row[2]

            full_name = number + ". " + problem_title
            if full_name + '.png' in os.listdir('screenshots'):
                continue

            runner.solve_problem(link, full_name)

    runner.solve_problem("https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/", "Minimum Number of Operations to Move All Balls to Each Box")