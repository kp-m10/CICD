import os
from flask import Flask, request, render_template
import boto3
from os.path import join
from flask.helpers import make_response

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/created',methods=['POST'])
def created():
    key1= request.form['key']
    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()
    save_data= []
    firstresponse= response['KeyPairs']
    for secondresponse in firstresponse:
         thirdresponse= secondresponse['KeyName']
         save_data.append(thirdresponse)
    if key1 in save_data:
         return render_template('notc.html', n=key1)
    else:
        ec2=boto3.resource('ec2')
        outfname = join(key1 + '.pem')
        outfile=open(outfname,'w')
        key_pair=ec2.create_key_pair(KeyName=key1)
        KeyPairOut = str(key_pair.key_material)
        print(KeyPairOut)
        outfile.write(KeyPairOut)
        return render_template('created.html' , n=key1)

@app.route('/display')
def display():
    ec21 = boto3.client('ec2')
    response = ec21.describe_key_pairs()
    save_data= []
    firstresponse= response['KeyPairs']
    for secondresponse in firstresponse:
         thirdresponse= secondresponse['KeyName']
         save_data.append(thirdresponse)
         print(save_data)
    return render_template('display.html',save=save_data)

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/deleted',methods=['POST'])
def deleted():
    ec22 = boto3.client('ec2')
    key2= request.form['key']
    response = ec22.delete_key_pair(KeyName=key2)
    return render_template('deleted.html',n1=key2)

@app.route('/vm_create',methods=['POST'])
def vm_create():
    return 0

if __name__== '__main__':    
    app.run(host="0.0.0.0", port=5000, debug=True)


