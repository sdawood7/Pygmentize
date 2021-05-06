import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--img_path", type=str)

flags = parser.parse_args()

print('Welcome to Pygmentize!')