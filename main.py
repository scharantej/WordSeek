
import random
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# Define the 4x4 grid with words
grid = [
    ['C', 'A', 'T', 'S'],
    ['D', 'O', 'G', 'R'],
    ['E', 'L', 'P', 'H'],
    ['A', 'N', 'T', 'S']
]

# List of valid words to be found in the grid
valid_words = ['CAT', 'DOG', 'RAT', 'HAT', 'PAN', 'TAN', 'ANTS']

# Keep track of the current game state
game_state = {
    'found_words': [],
    'selected_cells': [],
    'error_message': None
}

@app.route('/')
def index():
    return render_template('index.html', grid=grid, game_state=game_state)

@app.route('/validate_word', methods=['POST'])
def validate_word():
    # Get the word submitted by the player
    submitted_word = request.form['word'].upper()

    # Check if the word is valid
    if submitted_word in valid_words and submitted_word not in game_state['found_words']:
        # Add the word to the list of found words
        game_state['found_words'].append(submitted_word)

        # Clear the selected cells
        game_state['selected_cells'] = []

        # Return a success message
        return jsonify({'status': 'success', 'message': 'Congratulations! You found a word.'})
    else:
        # Return an error message
        return jsonify({'status': 'error', 'message': 'Invalid word or word already found.'})

@app.route('/reset_game')
def reset_game():
    # Clear the game state
    game_state['found_words'] = []
    game_state['selected_cells'] = []
    game_state['error_message'] = None

    # Redirect to the main page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
