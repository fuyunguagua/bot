class BotNet(object):
    def __init__(self, NAME, CNC, ID=0):
        self.attrs = {}
        self.attrs['NAME'] = NAME
        self.attrs['CNC'] = CNC
        self.attrs['ID'] = ID

    def __getitem__(self, item):
        return self.attrs[item]

    def __setitem__(self, key, value):
        self.attrs[key] = value

    def __str__(self):
        return '\n'.join(['{}:{}'.format(key, self.attrs[key]) for key in self.attrs])

Mirai = BotNet(NAME='Mirai', CNC='120.76.125.235')
Ares = BotNet(NAME='Ares', CNC='162.219.125.220')
BlackEnergy = BotNet(NAME='BlackEnergy', CNC='104.224.140.235')
Zeus = BotNet(NAME='Zeus', CNC='23.83.234.122')
Athena = BotNet(NAME='Athena', CNC='45.62.122.120')
botnet_list = [Mirai, Ares, BlackEnergy, Zeus, Athena]
with open('ip_map.csv') as f:
    for line in f:
        id = line[0:-1].split(' ')[0]
        ip = line[0:-1].split(' ')[1]
        for botnet in botnet_list:
            if botnet['CNC'] == ip:
                botnet['ID'] = int(id)


