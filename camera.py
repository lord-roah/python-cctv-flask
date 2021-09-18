import cv2
import cvui

from flask import Flask, render_template, Response

app = Flask(__name__)
ip=""
rtsp_username = ""
rtsp_password = ""
width = 800
height = 480
cam_no = 1
def create_camera (channel):
    rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@"+ip+"/Streaming/channels/" + channel + "02" #change the IP to suit yours
    cap = cv2.VideoCapture()
    cap.open(rtsp)
    cap.set(3, 640)  # ID number for width is 3
    cap.set(4, 480)  # ID number for height is 480
    cap.set(10, 100)  # ID number for brightness is 10qq
    return cap
    
def gen_frames():  # generate frame by frame from camera
    
    cam = create_camera(str(1))
	
    while True:
        # Capture frame-by-frame
       
        success, frame = cam.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
     
def gen_frames2(no):  # generate frame by frame from camera
    
    cam = create_camera(str(no))
	
    while True:
        # Capture frame-by-frame
       
        success, frame = cam.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result                  
 
                   
@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
                  
@app.route('/video_feed2')
def video_feed2():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames2(2), mimetype='multipart/x-mixed-replace; boundary=frame')
    
                 
@app.route('/video_feed3')
def video_feed3():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames2(3), mimetype='multipart/x-mixed-replace; boundary=frame')
    
                 
@app.route('/video_feed4')
def video_feed4():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames2(4), mimetype='multipart/x-mixed-replace; boundary=frame')
    
                  
@app.route('/video_feed5')
def video_feed5():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames2(5), mimetype='multipart/x-mixed-replace; boundary=frame')
    
                  
@app.route('/video_feed6')
def video_feed6():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames2(6), mimetype='multipart/x-mixed-replace; boundary=frame')
    
                 
@app.route('/video_feed7')
def video_feed7():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames2(7), mimetype='multipart/x-mixed-replace; boundary=frame')
    
                 
@app.route('/video_feed8')
def video_feed8():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames2(8), mimetype='multipart/x-mixed-replace; boundary=frame')
   


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
    

@app.route('/2')
def index2():
    """Video streaming home page."""
    return render_template('index2.html')
 
@app.route('/3')
def index3():
    """Video streaming home page."""
    return render_template('index3.html')
    

@app.route('/4')
def index4():
    """Video streaming home page."""
    return render_template('index4.html')
    
 
@app.route('/5')
def index5():
    """Video streaming home page."""
    return render_template('index5.html')
    

@app.route('/6')
def index6():
    """Video streaming home page."""
    return render_template('index6.html')
 

@app.route('/7')
def index7():
    """Video streaming home page."""
    return render_template('index7.html')
    

@app.route('/8')
def index8():
    """Video streaming home page."""
    return render_template('index8.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
