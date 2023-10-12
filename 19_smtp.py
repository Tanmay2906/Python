import smtplib

hostname = 'smtp.gmail.com'
email = 'bansaltanmay554@gmail.com'
password = 'mnbhteoenixqlivl'

with smtplib.SMTP(host=hostname) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs='tanmaybansal321@gmail.com',
        msg=f'Subject: Test Python Email\n\n Hi Paul, This is Python Email testing'
    )
