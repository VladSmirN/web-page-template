from form import PollForm
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_sh0uld_r3pl4ce_th1S'


@app.route('/')
def poll():
    poll_form = PollForm()
    return render_template('poll.html', form=poll_form)


@app.route('/result', methods=['GET', 'POST'])
def result():
    # Здесь получаем вывод модели и отображаем страничку результата
    return render_template('result.html', prediction=0)  # Вместо 0 должен быть ответ модели


if __name__ == '__main__':
    app.run()
