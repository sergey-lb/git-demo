import os
import waitress
from flask import Flask, render_template, request

from app.lib import collect_params_from_request_args, calculate_rolls_required, validate_params


def start():
    app = Flask(__name__)

    @app.route('/')
    def index():
        if not request.args:
            return render_template('index.html', user_input={})

        params = collect_params_from_request_args(request.args)
        error = validate_params(params)
        if error:
            return render_template('index.html', user_input=request.args, error=error)

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
