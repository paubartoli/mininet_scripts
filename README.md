
# mininet_scripts
EETAC - Planificació de Xarxes Use Case 2

## Environment 

- Ubuntu or another similar Linux distribution

## Prerequisites

- Download & install mininet
  - sudo apt-get install git
  - git clone git://github.com/mininet/mininet
  - ./mininet/util/install.sh
  
## Steps to configure the scenario

- git clone https://github.com/paubartoli/mininet_scripts

- import the desired topology:
  - mn --custom mininet_scripts/mininet_topology.py --topo mytopo 
  - mn --custom mininet_scripts/usecase2.py --topo mytopo
  
- To visualize graphically the enviroment we can use this link
  - http://demo.spear.narmox.com/app/?apiurl=demo#!/mininet 
- With the data extracted from the commands DUMP and LINKS of mininet
- Resulting the following topology:

   ![Topology](https://user-images.githubusercontent.com/70573576/116688564-2df3e500-a9b7-11eb-8f11-8d6ea549a48a.png)
