#!/usr/bin/python

from scapy.all import sr1,ISAKMP,IP,UDP,RandString,ISAKMP_payload_SA,ISAKMP_payload_Proposal
import sys

res = sr1( IP(dst="192.168.0.1")/UDP()
                /ISAKMP(init_cookie=RandString(8), exch_type="identity prot.")
                /ISAKMP_payload_SA(prop=ISAKMP_payload_Proposal()), timeout=2, verbose=0
              )

if res != None:
  print("Found IKE service:", res.summary())
else:
  print("No results")
  sys.exit(1)
