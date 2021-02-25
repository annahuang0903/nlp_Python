# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
filepath = 'birth_dev.tsv'
predicted_places = ['London'] * 500
total, correct = utils.evaluate_places(filepath, predicted_places)
print('Correct: {} out of {}: {}%'.format(correct, total, correct / total * 100))