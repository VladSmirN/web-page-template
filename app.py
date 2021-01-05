from form import PollForm
from flask import Flask, render_template ,request
import requests ,json ,logging,os
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_sh0uld_r3pl4ce_th1S'

if  os.path.isdir("./log") == False:
    os.makedirs("./log")
logging.basicConfig(filename=os.path.join("./log",'prediction.log') , level=logging.INFO)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def poll():
    poll_form = PollForm()
    return render_template('poll.html', form=poll_form)


@app.route('/result', methods=['GET', 'POST'])
def result():
    data = request.form.to_dict()
    data.pop('submit')
    data.pop('csrf_token')
    try:
        ans = requests.post('http://backend:5000/', json =json.dumps(data))
        logging.info('Prediction for  '+json.dumps(data)+' - '+ans.text)
        return render_template('result.html', prediction=ans.text)
    except:
         return render_template('fail.html')

if __name__ == '__main__':
    app.run()
