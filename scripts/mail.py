import getpass
import smtplib
from email.mime.text import MIMEText

from . import log


def sendmail(subject, body, fromaddr, toaddr, cc=None, rtcc=None, replyto=None):
    """Send mail."""

    if (fromaddr is not None) and (fromaddr.find("@") == -1):
        fromaddr = "%s@mit.edu" % fromaddr
    if (toaddr is not None) and (toaddr.find("@") == -1):
        toaddr = "%s@mit.edu" % toaddr
    if (cc is not None) and (cc.find("@") == -1):
        cc = "%s@mit.edu" % cc

    if log.unusual_locker():
        subject = "[%s] %s" % (log.get_tag(), subject)

    msg = MIMEText(body, _charset="utf-8")
    msg["From"] = fromaddr
    msg["Subject"] = subject
    msg["To"] = toaddr
    dests = [toaddr]
    if cc is not None:
        msg["CC"] = cc
        dests.append(cc)
    if rtcc is not None:
        msg["RT-Send-CC"] = rtcc
    if replyto is not None:
        msg["Reply-To"] = replyto

    s = smtplib.SMTP()
    s.connect()
    s.sendmail(getpass.getuser() + "@scripts.mit.edu", dests, msg.as_string())
    s.quit()


def create_ticket(subject, body, rtcc, requestor):
    sendmail(subject, body, requestor, "scripts@mit.edu", rtcc=rtcc)


def send_comment(subject, body, replyto, rtid, fromaddr, toaddr=None):
    if toaddr is not None:
        cc = "scripts-comment@mit.edu"
    else:
        toaddr = "scripts-comment@mit.edu"
        cc = None
    sendmail(
        "%s [help.mit.edu #%s]" % (subject, rtid),
        body,
        fromaddr,
        toaddr,
        cc=cc,
        replyto="scripts-comment@mit.edu, %s" % (replyto),
    )


def send_correspondence(subject, body, fromaddr, rtid):
    sendmail(
        "%s [help.mit.edu #%s]" % (subject, rtid), body, fromaddr, "scripts@mit.edu"
    )
