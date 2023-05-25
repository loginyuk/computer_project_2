from flask import *
from fileinput import filename
from compressor import compress

compressor = Flask(__name__)

path = ''
options_list= [{'algorithm' : 'LZW'}, {'algorithm' : 'LZ77'}, {'algorithm' : 'LZ78'}, \
         {'algorithm' : 'Deflate'}, {'algorithm' : 'Fifth algorithm'}]

@compressor.route('/')
def main():
    global options_list
    return render_template('main.html', options=options_list)

@compressor.route('/', methods = ['POST'])
def submit():
    global path
    global options_list
    if request.method == 'POST':  
        f = request.files['file']
        alg = list(request.form.values())
        f.save(f.filename)
        path = compress(f.filename, alg[0])
        return render_template('download.html', options=options_list)

@compressor.route('/download')
def download():
    global path
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    compressor.run()
