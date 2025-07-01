from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Game state stored in memory (not ideal for production)
game_state = {
    'user_score': 0,
    'computer_score': 0,
    'user_choice': 'rock',
    'computer_choice': 'rock',
    'result': '',
}

@app.route('/')
def index():
    return render_template('index.html', **game_state)

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form.get('choice')
    if user_choice not in ['rock', 'paper', 'scissors']:
        return redirect(url_for('index'))

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)

    # Update scores
    if result == 'win':
        game_state['user_score'] += 1
    elif result == 'lose':
        game_state['computer_score'] += 1

    # Save round data
    game_state['user_choice'] = user_choice
    game_state['computer_choice'] = computer_choice
    game_state['result'] = result

    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    game_state.update({
        'user_score': 0,
        'computer_score': 0,
        'user_choice': 'rock',
        'computer_choice': 'rock',
        'result': '',
    })
    return redirect(url_for('index'))

def determine_winner(user, computer):
    if user == computer:
        return 'draw'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return 'win'
    else:
        return 'lose'

if __name__ == '__main__':
    app.run(debug=True)
