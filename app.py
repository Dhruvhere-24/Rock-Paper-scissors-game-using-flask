from flask import Flask, render_template, request

app = Flask(__name__)

BUTTON_LAYOUT = [
    [{'label': 'AC', 'value': 'AC', 'class': 'function'},
     {'label': '+/-', 'value': '+/-', 'class': 'function'},
     {'label': '%', 'value': '%', 'class': 'function'},
     {'label': '÷', 'value': '/', 'class': 'operator'}],
    [{'label': '7', 'value': '7'}, {'label': '8', 'value': '8'}, {'label': '9', 'value': '9'},
     {'label': '×', 'value': '*', 'class': 'operator'}],
    [{'label': '4', 'value': '4'}, {'label': '5', 'value': '5'}, {'label': '6', 'value': '6'},
     {'label': '−', 'value': '-', 'class': 'operator'}],
    [{'label': '1', 'value': '1'}, {'label': '2', 'value': '2'}, {'label': '3', 'value': '3'},
     {'label': '+', 'value': '+', 'class': 'operator'}],
    [{'label': '0', 'value': '0', 'class': 'zero'}, {'label': '.', 'value': '.'},
     {'label': '=', 'value': '=', 'class': 'operator'}]
]

session_data = {
    'expression': ''
}

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        btn = request.form['button']
        expr = session_data.get('expression', '')

        if btn == 'AC':
            expr = ''
        elif btn == '=':
            try:
                expr = str(eval(expr))
            except:
                expr = 'Error'
        elif btn == '+/-':
            if expr.startswith('-'):
                expr = expr[1:]
            else:
                expr = '-' + expr
        else:
            expr += btn

        session_data['expression'] = expr

    # Convert internal symbols to user-friendly display
    expr_for_display = session_data.get('expression', '0') or '0'
    expr_for_display = expr_for_display.replace('*', '×').replace('/', '÷')

    return render_template("calculator.html", display=expr_for_display, buttons=BUTTON_LAYOUT)

if __name__ == '__main__':
    app.run(debug=True)
