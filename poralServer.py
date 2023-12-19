from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from portalDatabase import Database

class HospitalPortalHandler(BaseHTTPRequestHandler):
    
    def __init__(self, *args):
        self.database = Database()
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def do_POST(self):
        try:
            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_name = form.getvalue("patient_name")
                age = int(form.getvalue("patient_age"))
                admission_date = form.getvalue("admission_date")
                discharge_date = form.getvalue("discharge_date")

                self.database.addPatient(patient_name, age, admission_date, discharge_date)

                print("Patient added:", patient_name, age, admission_date, discharge_date)

                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1> Hospital's Portal </h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointment'>View Appointment </a>|\
                                  <a href='/dischargeDate'>Discharge Date</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient have been added</h3>")
                self.wfile.write(b"<div><a href='/addPatient'>Add a New Patient</a></div>")
                self.wfile.write(b"</center></body></html>")
                
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

        return

    
    def do_GET(self):
        try:

            if self.path == '/':
                data=[]
                records = self.database.getAllPatient()
                print(records)
                data=records
                
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointment'>View Appointment</a>|\
                                  <a href='/dischargeDate'>Discharge Date</a></div>")
                self.wfile.write(b"<hr><h2>All Patient</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Patient ID </th>\
                                        <th> Patient Name</th>\
                                        <th> Age</th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            
            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1> Hospital's Portal </h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointment'>View Appointment</a>|\
                                  <a href='/dischargeDate'>Discharge Date</a></div>")
                self.wfile.write(b"<hr><h2>Add New Patient</h2>")

                self.wfile.write(b"<form action='/addPatient' method='post'>")
                self.wfile.write(b'<label for="pname">Patient Name:</label>\
                      <input type="text" id="pname" name="pname"><br><br>\
                      <label for="owner_ssn">Age:</label>\
                      <input type="Number" id="Patientage" name="Patient_Age"><br><br>\
                      <label for="admission_date">Admission Date:</label>\
                      <input type="date"id="admission_date" name="admission_data"><br><br>\
                      <label for="discharge_date">Discharge Date:</label>\
                      <input type="date"id="discharge_date" name="discharge_data"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')

                       
                self.wfile.write(b"</center></body></html>")
                return
            if self.path == '/dischargeDate':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1> Hospital's Portal </h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointment'>View Appointment</a>|\
                                  <a href='/dischargeDate'>Discharge Date</a></div>")
                self.wfile.write(b"<hr><h2>Discharge Date</h2>")
                self.wfile.write(b"<form action='/addPatient' method='post'>")
                self.wfile.write(b'<label for="pname">Patient ID:</label>\
                      <input type="text" id="pname" name="pname"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')

                self.wfile.write(b"</center></body></html>")
                return
            
            if self.path =='/viewAppointment':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1> Hospital's Portal </h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                             <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointment'>View Appointment</a>|\
                                  <a href='/dischargeDate'>Discharge Date</a></div>")
                self.wfile.write(b"<hr><h2>View Appointment</h2>")

                self.wfile.write(b"</center></body></html>")
                return

            if self.path =='/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1> Hospital's Portal </h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                             <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointment'>View Appointment</a>|\
                                  <a href='/dischargeDate'>Discharge Date</a></div>")
                self.wfile.write(b"<hr><h2>Schedule Appointment</h2>")
                self.wfile.write(b"<form action='/addPatient' method='post'>")
                self.wfile.write(b'<label for="pname">Patient ID:</label>\
                      <input type="text" id="pname" name="pname"><br><br>\
                      <label for="dname">Doctor ID:</label>\
                      <input type="text" id="dname" name="dname"><br><br>\
                      <label for="admission_date">Appointment Date:</label>\
                      <input type="date"id="appointment_date" name="appointment_data"><br><br>\
                      <label for="admission_time">Appointment Time:</label>\
                      <input type="time"id="appointment_time" name="appointment_time"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')


                self.wfile.write(b"</center></body></html>")
                return
            
            if self.path =='/viewAppointment':
                return


            if self.path =='/dischargeDate':
                return



        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)




def run(server_class=HTTPServer, handler_class=HospitalPortalHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()

run()
