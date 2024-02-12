# Soluzione a distracted admin:
# 1) aprire il file con wireshark
# 2) analizzando il flusso http tra i vari stream si vede un pacchetto con una autorizzazione in base64
# 3) decodeficandola si ottiene la flag.
from base64 import b64decode
string='YWRtaW46ZmxhZ3t1bjRfcDRzc3cwcmRfdmVyYW0zbnRlX240c2Mwc3RhfQ=='
b64decode(string)
#b'admin:flag{un4_p4ssw0rd_veram3nte_n4sc0sta}'