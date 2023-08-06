import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from google.oauth2 import service_account


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'UTF-8').encode(), addr))


if __name__ == '__main__':
    from_addr = input('From: ')
    to_addr = input('To: ')

    msg = MIMEMultipart('alternative')
    msg['From'] = _format_addr('电子邮件调试者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('测试SMTP', 'utf-8').encode()

    # 附件
    msg.attach(MIMEText('Holy shit', 'plain', 'utf-8'))
    msg.attach(MIMEText('<html><body><h1>Holy shit,</h1>' +
                        '<p><img src="cid:0"></p>' +
                        '</body></html>', 'html', 'utf-8'))

    with open('test.jpg', 'rb') as f:
        mime = MIMEBase('image', 'jpg', filename='test.jpg')
        mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

    smtp_host = 'smtp.gmail.com'  # SMTP服务器的主机名
    smtp_port = 587  # SMTP服务器的端口号
    credentials = service_account.Credentials.from_service_account_file('C:/Users/uxiah/Downloads/credentials.json')
    with smtplib.SMTP(smtp_host, smtp_port, timeout=3000) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(credentials.service_account_email, 'dfce7ba495d6aaad7063e33e69852fb4df896e78')
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
