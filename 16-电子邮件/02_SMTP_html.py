import smtplib
from email.header import Header
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

    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = _format_addr('电子邮件调试者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('测试SMTP', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
