from flask import Flask,request,render_template
app=Flask(_name_)
@app.router('/register',methods=['GET','POST']
def register():
  if request.method =='POST';
  name =request.from['name']
  email =request.from['email']
  password =request.from['password']
  #store the user data into database or file
  return render_template('success.html')
  return render_template('register.html')
  if__name__=='__main__':
  app.run(host='0.0.0.0')
            
