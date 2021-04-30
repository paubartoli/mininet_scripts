"""UseCase 2 Topology"""
from mininet.topo import Topo
from mininet.link import TCLink


class MyTopo(Topo):

    def __init__(self, **opts):

        # Initialialize topology
        Topo.__init__(self, **opts)

        # Add hosts
        h1a = self.addHost('h1a', ip='10.0.0.2')
        h2p = self.addHost('h2p', ip='10.0.0.3')
        h3a = self.addHost('h3a', ip='10.0.0.4')
        h4p = self.addHost('h4p', ip='10.0.0.5')

        # Add SW
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add links
        self.addLink(h4p,s3, cls=TCLink, bw=1000, delay='10ms')
        self.addLink(h3a,s3, cls=TCLink, bw=1000, delay='10ms')
        self.addLink(s3,s1, cls=TCLink, bw=200, delay='100ms')
        self.addLink(s1,s2, cls=TCLink, bw=200, delay='100ms')
        self.addLink(s2,h2p, cls=TCLink, bw=1000, delay='10ms')
        self.addLink(s2,h1a, cls=TCLink, bw=1000, delay='10ms')

topos = { 'mytopo': (lambda: MyTopo() ) }

