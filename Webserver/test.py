from flask import Flask, render_template

app = Flask(__name__)

#rendering the HTML page which has the button
@app.route('/')
def json():
    return render_template('test.html')

#background process happening without any refreshing
@app.route('/red')
def red():
    print ("\nred")
    return ("nothing")

#background process happening without any refreshing
@app.route('/green')
def green():
    print ("\ngreen")
    return ("nothing")

#background process happening without any refreshing
@app.route('/blue')
def blue():
    print ("\nblue")
    return ("nothing")

#background process happening without any refreshing
@app.route('/teal')
def teal():
    print ("\nteal")
    return ("nothing")

#background process happening without any refreshing
@app.route('/purple')
def purple():
    print ("\npurple")
    return ("nothing")

#background process happening without any refreshing
@app.route('/orange')
def orange():
    print ("\norange")
    return ("nothing")

#background process happening without any refreshing
@app.route('/white')
def white():
    print ("\nwhite")
    return ("nothing")

#background process happening without any refreshing
@app.route('/alloff')
def alloff():
    print ("\nalloff")
    return ("nothing")



# @app.route("/")
# def main():
    # return render_template('index.html')

# @app.route("/about")
# def about():
    # return render_template('about.html')

# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(22, GPIO.OUT)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(24, GPIO.OUT)

# def alloffg():
	# GPIO.output(22, GPIO.HIGH)
	# GPIO.output(23, GPIO.HIGH)
	# GPIO.output(24, GPIO.HIGH)

# def redg(x):
	# if x == "off":
		# GPIO.output(22, GPIO.HIGH)
	# else:
		# GPIO.output(22, GPIO.LOW)

# def greeng(x):
	# if x == "off":
		# GPIO.output(23, GPIO.HIGH)
	# else:
		# GPIO.output(23, GPIO.LOW)

# def blueg(x):
	# if x == "off":
		# GPIO.output(24, GPIO.HIGH)
	# else:
		# GPIO.output(24, GPIO.LOW)

# def tealg(x):
	# if x == "off":
		# greeng('off')
		# blueg('off')
	# else:
		# for i in range(100):
			# greeng(None)
			# time.sleep(0.01)
			# greeng('off')
			# blueg(None)
			# time.sleep(0.01)
			# blueg('off')

# def purpleg(x):
	# if x == "off":
		# redg('off')
		# blueg('off')
	# else:
		# for i in range(100):
			# redg(None)
			# time.sleep(0.01)
			# redg('off')
			# blueg(None)
			# time.sleep(0.01)
			# blueg('off')

# def orangeg(x):
	# if x == "off":
		# red('off')
		# green('off')
	# else:
		# for i in range(100):
			# redg(None)
			# time.sleep(0.01)
			# redg('off')
			# greeng(None)
			# time.sleep(0.01)
			# greeng('off')

# def whiteg(x):
	# if x == "off":
		# redg('off')
		# greeng('off')
		# blueg('off')
	# else:
		# for i in range(1000):
			# redg(None)
			# time.sleep(0.001)
			# redg('off')
			# greeng(None)
			# time.sleep(0.001)
			# greeng('off')
			# blueg(None)
			# time.sleep(0.001)
			# blueg('off')





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
