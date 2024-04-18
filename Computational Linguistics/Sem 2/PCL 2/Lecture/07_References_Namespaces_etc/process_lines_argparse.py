import sys
import argparse


def parse_args():
   parser = argparse.ArgumentParser(description="Uppercase a specified number of lines from input file and print to outfile or stdout.")
   parser.add_argument("--input", type=argparse.FileType("r"), require=True, help="Input file")
   parser.add_argument("--num_lines", type=int, require=True, help="n lines to process")
   parser.add_argument("--output", type=argparse.FileType("w"), default=sys.stdout, help="outfile or stdout")
   return parser.parse_args()


def main():
   args = parse_args()

   # iterate over the lines in the input file
   for i, line in enumerate(args.input):
      # stop processing if we have processed the number of lines specified
      if i == args.num_lines:
         break
      # uppercase the line and write it to the output file
      args.output.write(line.upper())


if __name__ == "__main__":
    main()
