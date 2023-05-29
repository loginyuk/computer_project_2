from flask import *
from fileinput import filename
from compressor import compress
import os

compressor = Flask(__name__)

path = ''
options_list= [{'algorithm' : 'LZW'}, {'algorithm' : 'LZ77'}, {'algorithm' : 'Huffman'}, \
         {'algorithm' : 'Deflate'}, {'algorithm' : 'LZSS'}]

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


        output_folder = 'files'
        for filename in os.listdir(output_folder):
            file_path = os.path.join(output_folder, filename)
            # Check if the file is a regular file (not a directory)
            if os.path.isfile(file_path):
                # Remove the file
                os.remove(file_path)
        os.rmdir(output_folder)
        os.makedirs(output_folder)
    

        a = 'files/' + f.filename
        f.save(a)
        path, statistics = compress(a, alg[0])

        return render_template('download.html', options=options_list)

@compressor.route('/download')
def download():
    global path
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    compressor.run()
