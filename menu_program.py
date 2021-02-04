import speech_recognition as sr

print("Welcome to the Menu Program")
print('''
Here is the list of all the things you can ask for:
1) Hadoop
2) DSA
3) Machine Learning
4) Ansible
5) Python Concepts
6) AWS
7) Docker
8) Kubernetes
9) Networking Concepts
10) Linux Concepts
''')

print('So what would you like to start with?')

#speech recognition on what speaker is saying
r=sr.Recognizer()
with sr.Microphone() as source:
    print('Start saying...')
    audio=r.listen(source)
    print('speech done')
print('')
x=r.recognize_google(audio)
print('You:',x)


if 'Hadoop' in x or 'hadoop' in x:
    print("Can do!!")

if 'DSA' in x or 'data structure' in x or 'algorithm' in x:
    print("Can do!!")

if 'machine learning' in x or 'ML' in x:
    print("Can do!!")

if 'Ansible' in x or 'automation' in x:
    print("Can do!!")

if 'python' in x or 'programmin' in x or 'coding' in x:
    print("Can do!!")

if 'a w s' in x or 'Amazon' in x or 'cloud' in x:
    print("Can do!!")

if 'kubernetes' in x :
    print("Can do!!")

if 'network' in x :
    print("Can do!!")

if 'Linux' in x or 'Red Hat' in x or 'cent OS' in x:
    print('Can do!!')

else:
    print('')
    print("Couldn't hear you. Please try again using other keywords")
