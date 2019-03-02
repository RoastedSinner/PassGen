# Date: 02/23/2019
# Author: Mohamed
# Description: A password generator

max_count = 1000000

class PassGen:

    def __init__(self):
        self.pet = None
        self.child = None
        self.spouse = None
        self.target = None 
        self.passwords = []
    
    def prompt(self, txt):
        return str(input(txt))

    def question(self, target):
        answers = {}

        answers['firstname'] = self.prompt('Enter {}\'s first name: '.format(target))
        answers['lastname'] = self.prompt('Enter {}\'s last name: '.format(target))
        answers['nickname'] = self.prompt('Enter {}\'s nick name: '.format(target))

        while True:
            bday = self.prompt('Enter {}\'s birthday (dd.mm.yyyy): '.format(target))

            if not len(bday.strip()):
                break

            if len(bday.split('.')) != 3:
                print('Invalid birthday format\n')
                continue
            
            for _ in bday.split('.'):
                if not _.isdigit():
                    print('Birthday only requires numbers\n')
                    continue
            
            dd, mm, yyyy = bday.split('.')
            
            if int(mm) > 12 or int(mm) < 1 \
            or int(dd) > 31 or int(dd) < 1 \
            or len(yyyy) != 4:
                print('Invalid birthday\n')
                continue
            
            bday = { 'day': dd, 'month': mm, 'year': int(yyyy) }
            break 
            
        answers['birthday'] = bday
        return answers   

    def cases(self, word):
        return [word.lower(), word.title()]    
    
    def fullname(self, fname, lname):
        return ['{}{}'.format(a, b) for a in self.cases(fname) for b in self.cases(lname)]

    def format_names(self):                        
        for _ in range(1000):
            print(f'Generated: {len(self.passwords)}')

            iters = 0
            for data in [self.target, self.spouse, self.child, self.pet]:

                for n in ['firstname', 'lastname', 'nickname']:

                    fullname_list = []
                    name = data[n].strip()

                    if not len(name):
                        continue
                    
                    if not iters:
                        fullname_list = self.fullname(data['firstname'], data['lastname'])
                        iters += 1
                    
                    for word in self.cases(name) + fullname_list:

                        a, b, c = ('{}{}'.format(word, _), 
                                  '{}{}'.format(_, word), 
                                  '{0}{1}{0}'.format(_, word)
                                  )

                        if not word in self.passwords:
                            self.passwords.append(word)

                        if not a in self.passwords:
                            self.passwords.append(a)
                        
                        if not b in self.passwords:
                            self.passwords.append(b)

                        if not c in self.passwords:
                            self.passwords.append(c)

                        bday = data['birthday']

                        if bday:
                            d, e, f, g, h, i, j, k, l, m, n, o, p, q = (
                                '{}{}'.format(word, bday['year']),
                                '{}{}'.format(bday['year'], word),
                                '{}{}{}{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}{}.{}.{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}{}{}{}'.format(bday['day'], bday['month'], bday['year'], word),
                                '{}.{}.{}{}'.format(bday['day'], bday['month'], bday['year'], word),
                                '{}_{}{}{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}_{}.{}.{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}{}{}_{}'.format(bday['day'], bday['month'], bday['year'], word),
                                '{}.{}.{}_{}'.format(bday['day'], bday['month'], bday['year'], word),                                
                                '{}-{}{}{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}-{}.{}.{}'.format(word, bday['day'], bday['month'], bday['year']),
                                '{}{}{}-{}'.format(bday['day'], bday['month'], bday['year'], word),
                                '{}.{}.{}-{}'.format(bday['day'], bday['month'], bday['year'], word),

                            )

                            if not d in self.passwords:
                                self.passwords.append(d)
                            
                            if not e in self.passwords:
                                self.passwords.append(e)
                            
                            if not f in self.passwords:
                                self.passwords.append(f)

                            if not g in self.passwords:
                                self.passwords.append(g)   
   
                            if not h in self.passwords:
                                self.passwords.append(h)
      
                            if not i in self.passwords:
                                self.passwords.append(i)
                            
                            if not j in self.passwords:
                                self.passwords.append(j)
                            
                            if not k in self.passwords:
                                self.passwords.append(k)

                            if not l in self.passwords:
                                self.passwords.append(l)   
   
                            if not m in self.passwords:
                                self.passwords.append(m)

                            if not n in self.passwords:
                                self.passwords.append(n)
                            
                            if not o in self.passwords:
                                self.passwords.append(o)
                            
                            if not p in self.passwords:
                                self.passwords.append(p)

                            if not q in self.passwords:
                                self.passwords.append(q)     
        
    def generator(self):
        self.target = self.question('target')  
        print('\n')

        self.spouse = self.question('spouse')
        print('\n')

        self.child = self.question('child')
        print('\n')

        self.pet = self.question('pet')
        print('\n')

        print('Generating... \nIt\'s may take a while.')

        self.format_names()

        output_file = '{}.txt'.format(self.target['firstname'].lower()
                             if self.target['firstname'] else 'pass.txt')

        with open(output_file, 'wt') as f:
            for pwd in self.passwords:
                print('Writing ...')
                f.write('{}\n'.format(pwd))

        with open(output_file, 'at') as f:
            i = 0
            while(i < max_count):
                print('Writing additional combinations ... {}/{}'.format(i*3, max_count*3))
                f.write('{}{}\n'.format(self.target['firstname'], i))
                f.write('{}{}\n'.format(self.target['lastname'], i))
                f.write('{}{}\n'.format(self.target['nickname'], i))
                i += 1

        print('Passwords Generated.')

        quit()

if __name__ == '__main__':
    PassGen().generator()
