from mininet.net import Mininet

from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch

from mininet.cli import CLI

from mininet.log import setLogLevel

from mininet.link import Link, TCLink

 

def topology():

        net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

        h1 = net.addHost( 'h1', ip="10.0.0.2/24", mac="00:00:00:00:00:01" )

        h2 = net.addHost( 'h2', ip="11.0.0.2/24", mac="00:00:00:00:00:02" )

        h3 = net.addHost( 'h3', ip="12.0.0.2/24", mac="00:00:00:00:00:03" )

        h4 = net.addHost( 'h4', ip="13.0.0.2/24", mac="00:00:00:00:00:04" )

        R = net.addHost( 'R')

        s1 = net.addSwitch( 's1')

        s2 = net.addSwitch( 's2')

        s3 = net.addSwitch( 's3')

        s4 = net.addSwitch( 's4')

        c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )


        net.addLink( R, s1 )

        net.addLink( R, s2 )

        net.addLink( R, s3 )

        net.addLink( R, s4 )

        net.addLink( h1, s1 )

        net.addLink( h2, s2 )

        net.addLink( h3, s3 )

        net.addLink( h4, s4 )

        net.build()

        c0.start()

        s1.start( [c0] )

        s2.start( [c0] )

        s3.start( [c0] )

        s4.start( [c0] )

        R.cmd("ifconfig R-eth0 0")

        R.cmd("ifconfig R-eth1 0")

        R.cmd("ifconfig R-eth2 0")

        R.cmd("ifconfig R-eth3 0")

        R.cmd("ifconfig R-eth0 hw ether 00:00:00:00:01:01")

        R.cmd("ifconfig R-eth1 hw ether 00:00:00:00:01:02")

        R.cmd("ifconfig R-eth2 hw ether 00:00:00:00:01:03")

        R.cmd("ifconfig R-eth4 hw ether 00:00:00:00:01:04")

        R.cmd("ip addr add 10.0.0.1/24 brd + dev R-eth0")

        R.cmd("ip addr add 11.0.0.1/24 brd + dev R-eth1")

        R.cmd("ip addr add 12.0.0.1/24 brd + dev R-eth2")

        R.cmd("ip addr add 13.0.0.1/24 brd + dev R-eth3")

        R.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")

        h1.cmd("ip route add default via 10.0.0.1")

        h2.cmd("ip route add default via 11.0.0.1")

        h3.cmd("ip route add default via 12.0.0.1")

        h4.cmd("ip route add default via 13.0.0.1")

        s1.cmd("ovs-ofctl add-flow s1 priority=1,arp,actions=flood")

        s1.cmd("ovs-ofctl add-flow s1 priority=65535,ip,dl_dst=00:00:00:00:01:01,actions=output:1")

        s1.cmd("ovs-ofctl add-flow s1 priority=10,ip,nw_dst=10.0.0.2,actions=output:2")

        s2.cmd("ovs-ofctl add-flow s2 priority=1,arp,actions=flood")

        s2.cmd("ovs-ofctl add-flow s2 priority=65535,ip,dl_dst=00:00:00:00:01:02,actions=output:1")

        s2.cmd("ovs-ofctl add-flow s2 priority=10,ip,nw_dst=11.0.0.2,actions=output:2")

        s3.cmd("ovs-ofctl add-flow s3 priority=1,arp,actions=flood")

        s3.cmd("ovs-ofctl add-flow s3 priority=65535,ip,dl_dst=00:00:00:00:01:03,actions=output:1")

        s3.cmd("ovs-ofctl add-flow s3 priority=10,ip,nw_dst=12.0.0.2,actions=output:2")

        s4.cmd("ovs-ofctl add-flow s4 priority=1,arp,actions=flood")

        s4.cmd("ovs-ofctl add-flow s4 priority=65535,ip,dl_dst=00:00:00:00:01:04,actions=output:1")

        s4.cmd("ovs-ofctl add-flow s4 priority=10,ip,nw_dst=13.0.0.2,actions=output:2")

        

        print "Opening Commandline interface"

        CLI( net )

 

        print "Stopping Network"

        net.stop()

      

if __name__ == '__main__':

    setLogLevel( 'info' )

    topology() 