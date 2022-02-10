import turtle
from turtle_curve.generator import NumberGenerator
from abc import ABC, abstractmethod

from typing import Callable


class StepGenerator(ABC):
	"""A class that will generate a single step of a curve"""

	@abstractmethod
	def step(self, d: int, t: turtle.Turtle) -> None:
		"""Take a single step"""


class ConstantStep(StepGenerator):
	"""Always takes a step of the same size but in different directions"""

	def __init__(self, step_size: float):
		self.step_size = step_size

	def step(self, d: int, t: turtle.Turtle) -> None:
		turn_angle = d * 36	# 360 degrees have been split in 10 equal parts
		t.left(turn_angle)
		t.forward(self.step_size)


class CurveGenerator:
	"""A class that can generate curves from a number generator"""

	def __init__(self, generator: NumberGenerator, step: StepGenerator):
		self.generator = generator
		self.step = step

		self.turtle = turtle.Turtle()

	def generate(self):
		"""Generate the curve"""
		for d in self.generator:
			self.step.step(d, self.turtle)
