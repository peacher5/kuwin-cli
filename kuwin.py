from random import randint
from urllib import parse, request
from sys import argv

def print_usage():
    print("\n  - KUWiN CLI -\n\n" +
            "     Usage:  %s <action> <username> <password>\n\n" % argv[0] +
            "   Actions:  list        --  See all of your login sessions.\n" +
            "             login       --  Login to KU Network.\n" +
            "             logout      --  Logout from KU Network.\n" +
            "             logout-all  --  Logout from all sessions.\n\n" +
            "   Example:  %s login b6010987654 mypassword" % argv[0])

def sessions_table(session_list):
    formatted_session_dict = {}

    for session_line in session_list:
        session_info = session_line.split('\t')
        timestamp = session_info[1].split()
        date_time = timestamp[2] + " " + timestamp[1] + " " + timestamp[5] + ", " + timestamp[3]
        formatted_session_dict.update({session_info[0]:date_time})

    ip_spaces = max(map(len, formatted_session_dict.keys())) + 6

    table_sep = "   +" + "-" * ip_spaces + "+---------------------------+"
    ip_topic = "IP Address".center(ip_spaces)
    date_topic = "Login Date/Time".center(27)
    table = table_sep + "\n   |" + ip_topic + "|" + date_topic + "|\n" + table_sep

    for ip, date_time in formatted_session_dict.items():
        table += "\n   |%s|   %21s   |" % (ip.center(ip_spaces), date_time)

    table += "\n" + table_sep
    return table

def run(action, user, password):
    URL = 'https://login.ku.ac.th/mobile2.php'
    SSID = '"KUWIN"'
    API_VERSION = '5'

    # idk how to get link speed on all OS. so..
    SPEED = str(randint(120,160)) + ' Mbps'

    headers = {'User-Agent': ''}

    if action == 'logout-all':
        action = 'logoutuser'
        postData = {'username': user, 'password': password, 'ssid': SSID, 'speed': SPEED, 'v': API_VERSION, 'targetip': 'all'}
    else:
        postData = {'username': user, 'password': password, 'ssid': SSID, 'speed': SPEED, 'v': API_VERSION}

    try:
        data = parse.urlencode(postData).encode('ascii')
        req = request.Request(URL + '?action=' + action, data, headers)
        with request.urlopen(req) as response:
            data_response = response.read().decode('utf-8')
    except Exception as e:
        print("\n  Error: " + str(e))
        return

    info = data_response.split('\n')
    if 'OK' == info[0]:
        if action == 'login':
            print("\n   You have successfully logged in.")
        elif action == 'logout':
            print("\n   You have successfully logged out.")
        elif action == 'logoutuser':
            print("\n   You have successfully logged out on all sessions.")
        elif 'OK' == info[1]:
            # OK in second line => You have login sessions.
            session_count = len(info) - 4
            if session_count == 1:
                s = ""
            else:
                s = "s"
            print("\n   You have %d login session%s.\n" % (session_count, s))
            print(sessions_table(info[3:-1]))
        else:
            print("\n   You have no login sessions.")

    elif 'Invalid user/pass' == info[0]:
        print("\n   Your username & password is incorrect.")

    else:
        # In case they update API.
        print("\n   Unknown response from server:\n")
        print(data_response)

def init():
    action_list = ['list', 'login', 'logout', 'logout-all']
    arg_size = len(argv)
    if arg_size > 1:
        action = argv[1]
        if action in action_list:
            if arg_size == 4:
                user = argv[2]
                password = argv[3]
                run(action, user, password)
                return
            if arg_size < 4:
                print("\n   You must specify your username & password.")
                return
    print_usage()

if __name__ == "__main__":
    init()
