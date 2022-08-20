import json
import socket
import requests


def v4(ip_type='global'):
    """
    查询 ipv4 地址
    :param ip_type: string
    :type ip_type: local or global
    :return: ipv4
    :rtype: string
    """
    ipv4 = '0.0.0.0'
    try:
        if ip_type == 'local':
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ipv4 = s.getsockname()[0]
            s.close()
        elif ip_type == "global":
            url = "https://api-ipv4.ip.sb/ip"
            payload = {}
            headers = {'user-agent': 'Mozilla'}
            response = requests.request("GET", url, headers=headers, data=payload)
            ipv4 = response.text.strip().replace("\n","")
    except:
        pass
    return ipv4


def v6(ip_type='global'):
    """
    查询 ipv6 地址
    :param ip_type: string
    :type ip_type: local or global
    :return: ipv6
    :rtype: string
    """
    host_ipv6 = []
    try:
        if ip_type == 'local':
            ips = socket.getaddrinfo(socket.gethostname(), 80)
            for ip in ips:
                # 不是国内公网地址
                if ip[4][0].startswith('24') is False:
                    # 2408 中国联通\2409 中国移动\240e 中国电信
                    host_ipv6.append(ip[4][0])
        elif ip_type == 'global':
            url = "https://api-ipv6.ip.sb/ip"
            payload = {}
            headers = {'user-agent': 'Mozilla'}
            response = requests.request("GET", url, headers=headers, data=payload)
            host_ipv6.append(response.text)
    except:
        host_ipv6.append("::")
    ip = list(set(host_ipv6))[0]
    return ip


def info(ip=""):
    """
    获取 ip info
    :param ip: ipv4地址，为空则是本机公网ipv4
    :type ip: string
    :return: ip_info
    :rtype: json
    """
    url = "https://api.ip.sb/geoip/" + str(ip)
    payload = {}
    headers = {'user-agent': 'Mozilla'}

    response = requests.request("GET", url, headers=headers, data=payload)
    ip_info = json.loads(response.text)
    return ip_info

