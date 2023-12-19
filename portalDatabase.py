import mysql.connector
from mysql.connector import Error

class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="hospital_portal",
                 user='root',
                 password='March.2021'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            
            if self.connection.is_connected():
                return

        except Error as e:
            print("Error while connecting to MySQL", e)

    def addPatient(self, patient_name, age, admission_date, discharge_date):
        ''' Method to insert a new patient into the patients table '''
        try:
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "INSERT INTO patients (patient_name, age, admission_date, discharge_date) VALUES (%s, %s, %s, %s)"
                self.cursor.execute(query, (patient_name, age, admission_date, discharge_date))
                self.connection.commit()

        except Error as e:
            print("Error while adding patient:", e)

        finally:
            if self.cursor:
                self.cursor.close()


    def getAllPatient(self):
        ''' Method to get all patients from the patients table '''
        try:
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "SELECT * FROM patients"
                self.cursor.execute(query)
                records = self.cursor.fetchall()
                return records
            
        except Error as e:
            print("Error while getting all patients:", e)

        finally:
            if self.cursor:
                self.cursor.close()


    def scheduleAppointment(self, patient_id, doctor_id, appointment_date, appointment_time):
         if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO accounts (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
            values = (patient_id, doctor_id, appointment_date, appointment_time)
            self.cursor.execute(query, values)
            self.connection.commit()
    
            ''' Complete the method to Schedule Appointment'''
    pass

    def viewAppointments(self):
         if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "CALL viewAppointments(%s)"
            pa = (patient_id)
            self.cursor.execute(query, pa)
            results = self.cursor.fetchall()
            return results
        
            ''' Complete the method to call Appointments'''
    pass

    def dischargePatient(self, patient_id):
         if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "Discharge Patient WHERE patient_id = %s"
            params = (patient_id)
            self.cursor.execute(query, params)
            self.connection.commit()
           - ''' Complete the method to discharge a patient'''      
    pass
