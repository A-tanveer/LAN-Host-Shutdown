# import logging

# import math

import errno

from scapy.all import *

import scapy.config

import scapy.layers.l2

import scapy.route

import scapy.utils

import socket

logging.basicConfig(format='%(asctime)s %(levelname)-5s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def long2net(arg):
    if arg <= 0 or arg >= 0xFFFFFFFF:
        raise ValueError("illegal netmask value", hex(arg))
    return int(32 - round(math.log(0xFFFFFFFF - arg + 1, 2)))


def to_CIDR_notation(bytes_network, bytes_netmask):
    network = scapy.utils.ltoa(bytes_network)
    netmask = long2net(bytes_netmask)
    net = "%s/%s" % (network, netmask)
    if netmask < 22:
        logger.warn("%s is too big. Skipping..." % net)
        return None
    return net


def scan_and_print_neighbours(net, interface, timeout=1):
    logger.info("arping %s on %s" % (net, interface))
    #logger.info("network %s", net)
    try:
        ans, unans = scapy.layers.l2.arping(net, iface=interface, timeout=timeout, verbose=True)
        for s, r in ans.res:
            line = r.sprintf("%Ether.src%  %ARP.psrc%")
            try:
                hostname = socket.gethostbyaddr(r.psrc)
                line += " " + hostname[0]
            except socket.herror:
                # he has failed
                pass
            logger.info(line)
    except socket.error as e:
        if e.errno == errno.EPERM:
            logger.error("%s. Did you run as root?", e.strerror)
        else:
            raise
    return None


def log_ip_with_hostname():
    for network, netmask, _, interface, address in scapy.config.conf.route.routes:
        if network == 0 or interface == 'lo' or address == '58.57.132.1' or address == '0.0.0.0':
            continue

        if netmask <= 0 or netmask == 0xFFFFFFFF:
            continue

        net = to_CIDR_notation(network, netmask)

        if interface != scapy.config.conf.iface:
            logger.warn(
                "skipping %s because scapy currently doesn't support arping on non-primery network interfaces : %s" % (
                    net, interface))
            continue

        if net:
            scan_and_print_neighbours(net, interface)
