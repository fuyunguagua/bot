from botnet import botnet_list




if __name__ == '__main__':

    with open('finalscore.csv') as file:
        li = []
        for line in file:
            id = line[0:-1].split(',')[0]
            score = float(line[0:-1].split(',')[1])
            li.append((id,score))

        for index, key in enumerate(li):
            for item in botnet_list:
                if int(key[0]) == item['ID']:
                    item['RANK'] = index + 1

        for item in botnet_list:
            print '*' * 50
            print item

'''
CREATE TABLE `filterip` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `IP` char(15) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''