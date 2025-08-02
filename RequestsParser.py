class RequestsParser:
    def __init__(self):
        self.headers = None
        self.data = None
        self.host = None 
        self.path = None
        self.fileContent = None
        self.method = None

    def parse(self,filePath):
        with open(filePath,'r') as f:
            lines = [line.strip() for line in f.readlines()]
            self.fileContent = lines

        self.setHeaders(lines)
        self.setData(lines)
        
        self.host = self.headers['Host']
        self.path = lines[0].split()[1]
        self.method = lines[0].split()[0]
    
    def prettyPrint(self):
        print(self.fileContent[0])
        for header in self.headers:
            print(header + ': ' + self.headers[header])
        
        print()
        dText = ''
        for d in self.data:
            dText += d + '=' + self.data[d] + '&'

        dText = dText[0:len(dText) - 1]
        print(dText)

        print('\nHost: ' + self.host)
        print('Path: ' + self.path)
        print('Method:' + self.method)

    def setData(self,lines):
        self.data = {}
        datas = []

        for line in lines:
            if '=' in line and ':' not in line and '?' not in line:
                if '&' in line:
                    datas = line.split('&')
                else:
                    self.data[line.split('=')[0]] = line.split('=')[1]
        
        for d in datas:
            self.data[d.split('=')[0]] = d.split('=')[1]
    
    def setHeaders(self,lines):
        self.headers = {}
        for line in lines:
            if ':' in line:
                header = line.split(':',1)
                self.headers[header[0].strip()] = header[1].strip()
    
    #TODO add 3 method to change, add, and delete headers. If possible make it so that it can modify the data too.
