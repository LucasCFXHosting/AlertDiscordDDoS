export packet

interface=eth0
dumpdir=/root/dumps

while /bin/true; do
  pkt_old=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`
  sleep 1
  pkt_new=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`

  pkt=$(( $pkt_new - $pkt_old ))
  echo -ne "\rCurrent pp/s $pkt\033[0K"

  if [ $pkt -gt 5000 ]; then
    echo -e "\n`date`Capturing Attack..."
    packet="dump_`date +%d-%m-%y_%H:%M:%S`.pcap"
    tcpdump -i $interface -t -w $dumpdir/dump_`date +%d-%m-%y_%H:%M:%S`.pcap -c 10000
    echo "`date` Sleeping..."
python3 detected.py
  sleep 30 # TEMPS DE SLEEP QUAND l'EMBED MITIGEE S'ENVOI
python3 mitigated.py
  fi
done