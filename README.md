ACI-FastStrike – Automate Tenant creation for new Acquisitions / Mergers
	
•	This ansible playbook allows you to parse a CSV file that includes the needed attributes to automate and orchestrate creation of new tenants.  Ansible uses playbooks written in YAML to define the tasks we want to execute against an ACI fabric and the CSV file will be converted to YAML. 
•	This Ansible Playbook was created for Atrium Health but is not specific to the healthcare industry.
•	ACI-Fastrike will eliminate the security risk with a hastily engineered merger of the disparate networks and implement “Zero-Trust” to protect and secure networks of both companies.  ACI-Fastrike can also enable compliance. Every business today has a compliance requirement such as HIPAA and PCI. For many compliance requirements having a secure segmented network is a basic tenet.

Use Case

Many of our customers are going through mergers and acquisitions.  In our region alone, Mission Health is being acquired by HCA, RedHat is being acquired by IBM, and Atrium Health has recently purchased Navicent Health.   
This Playbook was created for Atrium Health but can be used for any enterprise or any industry.  Atrium’s board has decided to grow through acquisitions and mergers.   To ensure security, governance, and compliance with local and federal regulations across environments, automation is needed for the on-boarding of newly acquired healthcare systems.    The goal of this script is to create two Tenants.  One for Development / Test and the second is for production.  


Dependencies

•	Required Python modules for your environment:
o	Import : CSV
o	Import : SYS
o	Import : YAML
•	Required CSV file :  aci-tnt-vrf-bd-epg-ctr.csv
•	Required Python code that parses CSV file and create YML input file: parse_csv.py
•	Required Ansible playbook file that creates ACI tenant profile: aci-tnt-vrf-bd-epg-ctr-v2.yml


Ansible Documentation Reference

•	Main Documentation Index: https://docs.ansible.com
•	Ansible Installation: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html	
•	Ansible Network Module - ACI:  https://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html	

