import os
import waitress
from flask import Flask, render_template, request

from app.lib import calculate_rolls_required, validate_params, format_params, \
    validate_roll_length


def start():
    app = Flask(__name__)

    @app.route('/')
    def index():
        if not request.args:
            return render_template('index.html', user_input={})

        errors = validate_params(request.args)
        if len(errors) == 0:
            params = format_params(request.args)
            errors = validate_roll_length(params['roll_length'], params['room_height'], params['pattern_shift'])

        if len(errors):
            return render_template('index.html', user_input=request.args, errors=errors)

        rolls_required = calculate_rolls_required(
            params['room_length'],
            params['room_width'],
            params['room_height'],
            params['roll_width'],
            params['roll_length'],
            params['pattern_shift']
        )
        return render_template('index.html', user_input=request.args, rolls_required=rolls_required)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()