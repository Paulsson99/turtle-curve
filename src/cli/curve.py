from argparse import ArgumentParser

from turtle_curve.generator import FractionGenerator
from turtle_curve.turtle_walk import ConstantStep, CurveGenerator


def fraction_generator(args):
	"""Return a fraction generator from the aruments"""
	print(args)
	return FractionGenerator(args.n, max_iter=args.max)


def main():
	parser = ArgumentParser(description="This program will generate beautiful curves form numbers")
	parser.add_argument(
		"-m", 
		"--max", 
		type=int, 
		help="Maximum iterations allowed for the turtle walk", 
		default=1000
	)

	subparsers = parser.add_subparsers(
		help="There are many ways to generate numbers. Pick one of them.", 
		dest="prog", 
		required=True
	)

	# Fraction parser
	fraction_parser = subparsers.add_parser(
		"fraction", 
		help="Generate a series of numbers from the decimal expansion of a fraction 1/n"
	)
	fraction_parser.add_argument("n", type=int, help="The intger n that will generate the fraction 1/n")

	# Parse the args
	args = parser.parse_args()

	if args.prog == "fraction":
		generator = fraction_generator(args)

	step = ConstantStep(10)
	curve = CurveGenerator(generator, step)

	curve.generate()


if __name__ == '__main__':
	main()