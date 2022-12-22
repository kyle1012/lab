import os
import json
import PyPDF2
from flask import Flask, request, make_response, jsonify, abort, send_file
from flask_mysqldb import MySQL
from flask_cors import CORS
from dotenv import load_dotenv
from tika import parser
from datetime import datetime


load_dotenv()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
mysql = MySQL(app)

app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

def on_json_loading_failed_return_dict(e):
	return {}

@app.route('/login', methods=['POST','GET']) 
def users():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    user_data = {}
    data1 = request.get_json()
    username = data1.get('username')
    password = data1.get('password')

    user_data = {
        "username" : username,
        "password" : password
    }
#        user_data = user_model.User.query.filter_by(username=username).first()
#        if user_data is not None:
#        my_logger.info("Username is Already exist")
#        return {"success": "username is already exist"}
    cur = mysql.connection.cursor() 
    cur.execute('SELECT * FROM user WHERE id = %s AND password = %s', (username, password))
    account = cur.fetchone()
    if account is not None:
        return ("로그인 성공",200)
    else :
        return ("ID와 Password를 확인해주세요",500)
        #rv = cur.fetchall()
        #mysql.connection.commit()
    cur.close()


@app.route('/upload', methods=['GET','POST','OPTIONS'])
def upload():
    #result = request.form
    #return result
    #return make_response(jsonify(success=True), 200)
    files = request.files.getlist('file')
    data = {}
    dt_datetime = datetime.now()
    format = '%X'
    str_datetime = datetime.strftime(dt_datetime,format)
    for f in files:
        f.file_name, f.file_ext = os.path.splitext(f.filename)
        ip_file_path = f.file_name + "_" + str_datetime + f.file_ext
        f.save('/lab/public/IP_Doc/' + ip_file_path)
        file_path = '/lab/public/IP_Doc/' + ip_file_path
        parsed = parser.from_file(file_path)
        text = parsed['content'].strip()
        txt = text.split('\n\n')
        z=[s for s in txt if "요청사유" in s]
        zz = (''.join(z))
        zzz = txt.index(zz)
        x=[s for s in txt if "[참고사항]" in s]
        xx = (''.join(x))
        xxx = txt.index(xx)
        a = list(filter(lambda x: '기\t\t\t안\t\t\t자' in x,txt))[0][10:]
        bb =  list(filter(lambda x: '유선MAC주소' in x,txt))[0][8:]
        b = bb.replace('-',':')
        cc = list(filter(lambda x: '무선MAC주소' in x,txt))[0][8:]
        c = cc.replace('-',':')
        d = list(filter(lambda x: '기\t안\t부\t서' in x,txt))[0][8:]
        #if len(list(filter(lambda x: '이메일' in x,txt))[0]) >4:
        #    print(list(filter(lambda x: '이메일' in x,txt))[0][4:].split('@')[0])
        #else:
        #    print("이메일 미존재")
        e = list(filter(lambda x: '이메일' in x,txt))[0][4:]
        f = list(filter(lambda x: '문\t서\t번\t호' in x,txt))[0][8:]
        ip_title = list(filter(lambda x: '제\t\t\t\t\t\t\t\t\t목' in x,txt))[0][12:]
        ip_draft_time = list(filter(lambda x: '기\t\t\t안\t\t\t일' in x,txt))[0][10:]
        g = (''.join(txt[zzz+1:xxx]))
        dic = dict(peo = a, mac1 = b, mac2 = c, dep = d, email = e, num = f, whyy = g, file_path = file_path, title = ip_title, time = ip_draft_time, file_name = ip_file_path)
        data = json.dumps(dic, ensure_ascii=False)
    return make_response(data, 200)
    '''elif s for s in txt if "인터넷\t차단\t해제\t신청서" in s:
            int_z=[s for s in txt if "요청사유" in s]
            int_zz = (''.join(z))
            int_zzz = txt.index(zz)
            int_a = list(filter(lambda x: '기\t\t\t안\t\t\t자' in x,txt))[0][10:]
            int_b = list(filter(lambda x: '신청\tIP주소' in x,txt))[0][8:]
            int_c = list(filter(lambda x: '기간 ' in x,txt))[0][3:]
            int_d = list(filter(lambda x: '기\t안\t부\t서' in x,txt))[0][8:]
            int_e = txt[int_zzz+1]
            int_f = txt[int_zzz+2]
            int_g = list(filter(lambda x: '문\t서\t번\t호' in x,txt))[0][8:]
            int_dic = dict(int_peo = int_a, int_ip = int_b, int_period = int_c, int_dep = int_d, int_site = int_e, int_why = int_f, int_doc = int_g)
            int_data = json.dumps(dic, ensure_ascii=False)
            return make_response(int_data, 200)
        else:
            return "문서를 확인해주세요"'''
    #dfs = tabula.read_pdf(file_path + '.pdf', pages='all')
    #print(dfs[0])
    #return
@app.route('/insert', methods=['POST','GET']) 
def insert():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    ip_data = request.get_json()
#        user_data = user_model.User.query.filter_by(username=username).first()
#        if user_data is not None:
#        my_logger.info("Username is Already exist")
#        return {"success": "username is already exist"}
    now = datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M')
    cur = mysql.connection.cursor() 
    cur.execute('INSERT INTO IP_App (ip, doc_division, form, title, user, mac1, mac2, division, dep, email, purpose, terminal, why, doc, d_time, manager, file_path, now_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (ip_data['db_ip'], "IP신청서", ip_data['db_form'], ip_data['db_title'], ip_data['db_user'], ip_data['db_mac1'], ip_data['db_mac2'], ip_data['db_division'], ip_data['db_dep'], ip_data['db_email'], ip_data['db_purpose'], ip_data['db_terminal'], ip_data['db_why'], ip_data['db_doc'], ip_data['db_time'], ip_data['db_manager'], ip_data['db_file_path'], now_time))
    #account = cur.fetchone()
    #if account is not None:
    #    return ("로그인 성공",200)
    #else :
    #    return ("ID와 Password를 확인해주세요",500)
        #rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return ("업로드 성공", 200)

@app.route('/board', methods=['POST','GET']) 
def board():
    cur = mysql.connection.cursor()
    cur.execute("select * from IP_App")

    board_list = cur.fetchall()
    cur.close()
    board_list = sorted(board_list,reverse = True)
    for row in board_list:
        data_list = json.dumps(board_list, ensure_ascii=False)

    return data_list
    


@app.route('/download', methods=['GET','POST']) 
def download():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    primary_no = request.get_json()
    primary_key = primary_no['id']
    cur = mysql.connection.cursor()
    cur.execute("select file_path from IP_App where no = %s", [primary_key])
    detail_list = cur.fetchone()
    cur.close()
    all_list = json.dumps(detail_list, ensure_ascii=False)
    #print(type(all_list))
    sl_list = all_list[2:-2]
    file_name = f"{sl_list}"
    return send_file(file_name,
                     mimetype='application/pdf',
                     download_name='download_file',
                     as_attachment=True)

@app.route('/update', methods=['GET','POST']) 
def update():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    update_data = request.get_json()
    cur = mysql.connection.cursor()
    if (update_data['db_division_doc'] == "IP신청서"):
        ip_sql = 'UPDATE IP_App SET ip=%s, mac1=%s, mac2=%s, division=%s, email=%s, purpose=%s, terminal=%s, why=%s, doc=%s where no=%s'
        cur.execute(ip_sql, (update_data['db_ip'], update_data['db_mac1'], update_data['db_mac2'], update_data['db_division'], update_data['db_email'], update_data['db_purpose'], update_data['db_terminal'], update_data['db_why'], update_data['db_doc'], update_data['db_no']))
        mysql.connection.commit()
        cur.close()
        return ("업로드 성공", 200)
    elif (update_data['db_division_doc'] == "방화벽정책신청서"):
        firewall_sql = 'UPDATE IP_App SET firewall=%s, term=%s, policy=%s, why=%s, doc=%s where no=%s'
        cur.execute(firewall_sql, (update_data['db_firewall'], update_data['db_period'], update_data['db_policy'], update_data['db_why'], update_data['db_doc'], update_data['db_no']))
        mysql.connection.commit()
        cur.close()
        return ("업로드 성공", 200)
    elif (update_data['db_division_doc'] == "인터넷차단해제신청서"):
        firewall_sql = 'UPDATE IP_App SET ip=%s, term=%s, site=%s, why=%s, doc=%s where no=%s'
        cur.execute(firewall_sql, (update_data['db_ip'], update_data['db_period'], update_data['db_site'], update_data['db_why'], update_data['db_doc'], update_data['db_no']))
        mysql.connection.commit()
        cur.close()
        return ("업로드 성공", 200)
    elif (update_data['db_division_doc'] == "계정신청서"):
        firewall_sql = 'UPDATE IP_App SET ip=%s, term=%s, vpn_account=%s, why=%s, doc=%s where no=%s'
        cur.execute(firewall_sql, (update_data['db_ip'], update_data['db_period'], update_data['db_vpn'], update_data['db_why'], update_data['db_doc'], update_data['db_no']))
        mysql.connection.commit()
        cur.close()
        return ("업로드 성공", 200)

@app.route('/int_upload', methods=['GET','POST','OPTIONS'])
def int_upload():
    #result = request.form
    #return result
    #return make_response(jsonify(success=True), 200)
    files = request.files.getlist('file')
    data = {}
    dt_datetime = datetime.now()
    format = '%X'
    str_datetime = datetime.strftime(dt_datetime,format)
    for f in files:
        f.file_name, f.file_ext = os.path.splitext(f.filename)
        internet_file_path = f.file_name + "_" + str_datetime + f.file_ext
        f.save('/lab/public/INTERNET_Doc/' + internet_file_path)
        int_file_path = '/lab/public/INTERNET_Doc/' + internet_file_path
        parsed = parser.from_file(int_file_path)
        text = parsed['content'].strip()
        txt = text.split('\n\n')
        z=[s for s in txt if "요청사유" in s]
        zz = (''.join(z))
        zzz = txt.index(zz)
        x=[s for s in txt if "[참고사항]" in s]
        xx = (''.join(x))
        xxx = txt.index(xx)
        p=[s for s in txt if "기간 " in s]
        pp = (''.join(p))
        ppp = txt.index(pp)
        pi=[s for s in txt if "신청\tIP주소" in s]
        pi2 = (''.join(pi))
        pi3 = txt.index(pi2)
        int_a = list(filter(lambda x: '기\t\t\t안\t\t\t자' in x,txt))[0][10:]
        int_pi = (''.join(txt[pi3:ppp]))
        b = int_pi.replace('\t',' ')
        int_b = b.replace("신청 IP주소","")
        #b = bb.replace('-',':')
        #print(b)
        per = list(filter(lambda x: '기간 ' in x,txt))[0][3:]
        c = per.replace('\t',' ')
        int_c = c.replace(" (최대 1년)","")
        int_d = list(filter(lambda x: '기\t안\t부\t서' in x,txt))[0][8:]
        int_site = txt[zzz+1]
        int_e = int_site.replace('\t',' ')
        int_why = (''.join(txt[zzz+2:xxx]))
        int_f = int_why.replace('\t',' ')
        int_g = list(filter(lambda x: '문\t서\t번\t호' in x,txt))[0][8:]
        int_title = list(filter(lambda x: '제\t\t\t\t\t\t\t\t\t목' in x,txt))[0][12:]
        int_draft_time = list(filter(lambda x: '기\t\t\t안\t\t\t일' in x,txt))[0][10:]
        dic = dict(int_peo = int_a, int_ip = int_b, int_period = int_c, int_dep = int_d, int_site = int_e, int_why = int_f, int_doc = int_g, int_file_path = int_file_path, int_title = int_title, int_time = int_draft_time,  file_name = internet_file_path)
        #dic = dict(peo = a, mac1 = b, mac2 = c, dep = d, email = e, num = f, whyy = g)
        data = json.dumps(dic, ensure_ascii=False)
    return make_response(data, 200)

@app.route('/int_insert', methods=['POST','GET']) 
def int_insert():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    int_data = request.get_json()
#        user_data = user_model.User.query.filter_by(username=username).first()
#        if user_data is not None:
#        my_logger.info("Username is Already exist")
#        return {"success": "username is already exist"}
    #int_db_file_path = '/lab/backend/internet_doc/' + int_file_path
    now = datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M')
    cur = mysql.connection.cursor() 
    cur.execute('INSERT INTO IP_App (ip, doc_division, form, title, user, dep, why, sort, term, site, doc, d_time, manager, file_path, now_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (int_data['db_ip'], "인터넷차단해제신청서", int_data['db_form'], int_data['db_title'], int_data['db_user'], int_data['db_dep'], int_data['db_why'], int_data['db_sort'], int_data['db_period'], int_data['db_site'], int_data['db_doc'], int_data['db_time'], int_data['db_manager'], int_data['db_file_path'], now_time))
    #account = cur.fetchone()
    #if account is not None:
    #    return ("로그인 성공",200)
    #else :
    #    return ("ID와 Password를 확인해주세요",500)
        #rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return ("업로드 성공", 200)

@app.route('/firewall_upload', methods=['GET','POST','OPTIONS'])
def firewall_upload():
    #result = request.form
    #return result
    #return make_response(jsonify(success=True), 200)
    files = request.files.getlist('file')
    data = {}
    dt_datetime = datetime.now()
    format = '%X'
    str_datetime = datetime.strftime(dt_datetime,format)
    for f in files:
        f.file_name, f.file_ext = os.path.splitext(f.filename)
        firewall_file_path = f.file_name + "_" + str_datetime + f.file_ext
        f.save('/lab/public/FIREWALL_Doc/' + firewall_file_path)
        db_file_path = '/lab/public/FIREWALL_Doc/' + firewall_file_path
        parsed = parser.from_file(db_file_path)
        text = parsed['content'].strip()
        txt = text.split('\n\n')
        z=[s for s in txt if "방화벽\n정책" in s]
        zz = (''.join(z))
        zzz = txt.index(zz)
        x=[s for s in txt if "요청사유\n(상세기술)" in s]
        xx = (''.join(x))
        xxx = txt.index(xx)
        a = list(filter(lambda x: '기\t\t\t안\t\t\t자' in x,txt))[0][10:]
        #b = bb.replace('-',':')
        #print(b)
        per = list(filter(lambda x: '기간 ' in x,txt))[0][3:]
        cc = per.replace('\t',' ')
        c = cc.replace(" (최대 1년)","")
        d = list(filter(lambda x: '기\t안\t부\t서' in x,txt))[0][8:]
        policy = txt[zzz+1]
        e = policy.replace('\t',' ')
        why = txt[xxx+1]
        f = why.replace('\t',' ')
        doc = list(filter(lambda x: '문\t서\t번\t호' in x,txt))[0][8:]
        title= list(filter(lambda x: '제\t\t\t\t\t\t\t\t\t목' in x,txt))[0][12:]
        draft_time = list(filter(lambda x: '기\t\t\t안\t\t\t일' in x,txt))[0][10:]
        dic = dict(peo = a, period = c, dep = d, policy = e, why = f, doc = doc, file_path = db_file_path, title = title, time = draft_time, file_name = firewall_file_path)
        #g = (''.join(txt[zzz+1:xxx]))
        #dic = dict(peo = a, mac1 = b, mac2 = c, dep = d, email = e, num = f, whyy = g)
        data = json.dumps(dic, ensure_ascii=False)
    return make_response(data, 200)

@app.route('/firewall_insert', methods=['POST','GET']) 
def firewall_insert():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    data = request.get_json()
#        user_data = user_model.User.query.filter_by(username=username).first()
#        if user_data is not None:
#        my_logger.info("Username is Already exist")
#        return {"success": "username is already exist"}
    #int_db_file_path = '/lab/backend/internet_doc/' + int_file_path
    now = datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M')
    cur = mysql.connection.cursor() 
    cur.execute('INSERT INTO IP_App (doc_division, form, title, user, dep, why, firewall, policy, term, doc, d_time, manager, file_path, now_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', ("방화벽정책신청서", data['db_form'], data['db_title'], data['db_user'], data['db_dep'], data['db_why'], data['db_firewall'], data['db_policy'], data['db_period'], data['db_doc'], data['db_time'], data['db_manager'], data['db_file_path'], now_time))
    #account = cur.fetchone()
    #if account is not None:
    #    return ("로그인 성공",200)
    #else :
    #    return ("ID와 Password를 확인해주세요",500)
        #rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return ("업로드 성공", 200)


@app.route('/account_upload', methods=['GET','POST','OPTIONS'])
def account_upload():
    #result = request.form
    #return result
    #return make_response(jsonify(success=True), 200)
    files = request.files.getlist('file')
    data = {}
    dt_datetime = datetime.now()
    format = '%X'
    str_datetime = datetime.strftime(dt_datetime,format)
    for f in files:
        f.file_name, f.file_ext = os.path.splitext(f.filename)
        account_file_path = f.file_name + "_" + str_datetime + f.file_ext
        f.save('/lab/public/ACCOUNT_Doc/' + account_file_path)
        db_file_path = '/lab/public/ACCOUNT_Doc/' + account_file_path
        parsed = parser.from_file(db_file_path)
        text = parsed['content'].strip()
        txt = text.split('\n\n')
        z=[s for s in txt if "접근대상\tIP/Port" in s]
        zz = (''.join(z))
        zzz = txt.index(zz)
        x=[s for s in txt if "요청사유\n(상세기술)" in s]
        xx = (''.join(x))
        xxx = txt.index(xx)
        a = list(filter(lambda x: '기\t\t\t안\t\t\t자' in x,txt))[0][10:]
        #b = bb.replace('-',':')
        #print(b)
        per = list(filter(lambda x: '사용기간 ' in x,txt))[0][5:]
        cc = per.replace('\t',' ')
        c = cc.replace(" (VPN계정만 해당)","")
        d = list(filter(lambda x: '기\t안\t부\t서' in x,txt))[0][8:]
        accept = txt[zzz+1:xxx]
        acceptjoin = (''.join(accept))
        e = acceptjoin.replace('\t',' ')
        why = txt[xxx+1]
        f = why.replace('\t',' ')
        doc = list(filter(lambda x: '문\t서\t번\t호' in x,txt))[0][8:]
        title= list(filter(lambda x: '제\t\t\t\t\t\t\t\t\t목' in x,txt))[0][12:]
        draft_time = list(filter(lambda x: '기\t\t\t안\t\t\t일' in x,txt))[0][10:]
        dic = dict(peo = a, period = c, dep = d, accept = e, why = f, doc = doc, file_path = db_file_path, title = title, time = draft_time, file_name = account_file_path)
        #g = (''.join(txt[zzz+1:xxx]))
        #dic = dict(peo = a, mac1 = b, mac2 = c, dep = d, email = e, num = f, whyy = g)
        data = json.dumps(dic, ensure_ascii=False)
    return make_response(data, 200)


@app.route('/account_insert', methods=['POST','GET']) 
def account_insert():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    data = request.get_json()
    print(data)
#        user_data = user_model.User.query.filter_by(username=username).first()
#        if user_data is not None:
#        my_logger.info("Username is Already exist")
#        return {"success": "username is already exist"}
    #int_db_file_path = '/lab/backend/internet_doc/' + int_file_path
    now = datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M')
    cur = mysql.connection.cursor() 
    cur.execute('INSERT INTO IP_App (doc_division, form, title, user, dep, why, ip, term, doc, d_time, manager, file_path, now_time, vpn_account) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', ("계정신청서", data['db_form'], data['db_title'], data['db_user'], data['db_dep'], data['db_why'], data['db_ip'], data['db_period'], data['db_doc'], data['db_time'], data['db_manager'], data['db_file_path'], now_time, data['db_vpn']))
    #account = cur.fetchone()
    #if account is not None:
    #    return ("로그인 성공",200)
    #else :
    #    return ("ID와 Password를 확인해주세요",500)
        #rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return ("업로드 성공", 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)