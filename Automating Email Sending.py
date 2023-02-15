

# before testing start python email server
# python -m smtpd -c DebuggingServer -n localhost:1025

# Import smtplib for the actual sending function
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from datetime import datetime
import schedule

execution_time = '12:50:00'

_report_file = "./report.csv"

def create_dummy_report():
    with open(_report_file, "w") as report:
        report.write("My Report")

# email server configuration
email_server_config = {
    "host" : 'localhost',
    "port" : 1025,
    # "username" : 'user',
    # "password" : 'pass'
}

sender = 'admin@example.com'
receivers = ['info@example.com', "test@helloworld.com"]

def main():
    print(f"Current time: {str(datetime.now())}")
    # Creating dummpy report
    create_dummy_report()

    # constructing email message
    msg = MIMEMultipart()
    msg['Subject'] = 'Daily Report'
    msg['From'] = 'admin@example.com'
    msg['To'] = ", ".join(receivers)

    # message body
    body = MIMEText("Please find the attached")
    msg.attach(body)
    
    # Create MIMEApplication object to attach file
    with open(_report_file, 'r') as f:
        part = MIMEApplication(f.read(), Name=basename(_report_file))
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(_report_file))
    msg.attach(part)
    
    # instantiate server and send email
    with smtplib.SMTP(email_server_config['host'], email_server_config['port']) as server:
        # server.login(email_server_config['username'], email_server_config['password'])
        server.sendmail(sender, receivers, msg.as_string())

if __name__ == '__main__':
    schedule.every().day.at(execution_time).do(main)

    while True:
        schedule.run_pending()

# logging
