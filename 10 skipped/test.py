import pcapkit
plist = pcapkit.extract(fin='icmps.pcap', fout='out.plist', format='plist', store=False)
json = pcapkit.extract(fin='icmps.pcap', fout='out.json', format='json', extension=False)
