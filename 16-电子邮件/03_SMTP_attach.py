import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'UTF-8').encode(), addr))


if __name__ == '__main__':
    from_addr = input('From: ')
    password = input('Password: ')
    to_addr = input('To: ')
    smtp_server = input('SMTP Server: ')
    content = input('Content(HTML): ')

    msg = MIMEMultipart()
    msg['From'] = _format_addr('电子邮件调试者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('测试SMTP', 'utf-8').encode()

    # 附件
    msg.attach(MIMEText(content, 'html', 'utf-8'))

    with open('test.jpg', 'rb') as f:
        mime = MIMEBase('image', 'jpg', filename='test.jpg')
        mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
